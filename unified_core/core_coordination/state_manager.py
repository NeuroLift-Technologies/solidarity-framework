"""
Unified State Manager - Centralized state management for the Agent Solidarity Kit
Manages shared state across all components while maintaining privacy and consistency
"""

import asyncio
import logging
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict
from enum import Enum
import hashlib
import os

class StateScope(Enum):
    """Scope of state data"""
    USER = "user"           # User-specific data
    SESSION = "session"     # Session-specific data
    GLOBAL = "global"       # Global system data
    COMPONENT = "component" # Component-specific data

class StateAccess(Enum):
    """Access levels for state data"""
    PUBLIC = "public"       # Accessible by all components
    PROTECTED = "protected" # Accessible by authorized components
    PRIVATE = "private"     # Accessible only by owning component
    ENCRYPTED = "encrypted" # Encrypted storage

@dataclass
class StateEntry:
    """Individual state entry"""
    key: str
    value: Any
    scope: StateScope
    access: StateAccess
    owner: str
    created: datetime
    modified: datetime
    version: int
    metadata: Dict[str, Any]

class UnifiedStateManager:
    """
    Unified State Manager for the Agent Solidarity Kit
    
    Provides centralized, secure, and consistent state management across
    all foundation components while maintaining privacy and data integrity.
    """
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.is_initialized = False
        
        # State storage
        self.state_store: Dict[str, StateEntry] = {}
        self.component_states: Dict[str, Dict[str, Any]] = {}
        self.session_data: Dict[str, Any] = {}
        self.global_state: Dict[str, Any] = {}
        
        # Access control
        self.component_permissions: Dict[str, List[str]] = {}
        self.access_log: List[Dict[str, Any]] = []
        
        # State synchronization
        self.state_locks: Dict[str, asyncio.Lock] = {}
        self.change_listeners: Dict[str, List[callable]] = {}
        self.sync_queue: List[Dict[str, Any]] = []
        
        # Performance tracking
        self.performance_metrics = {
            "total_operations": 0,
            "read_operations": 0,
            "write_operations": 0,
            "avg_operation_time": 0.0,
            "cache_hits": 0,
            "cache_misses": 0
        }
        
        self.logger = logging.getLogger(f"StateManager-{self.user_id}")
        
    async def initialize(self) -> bool:
        """Initialize the state manager"""
        try:
            # Set up component permissions
            await self._setup_component_permissions()
            
            # Initialize state storage
            await self._initialize_state_storage()
            
            # Load persistent state
            await self._load_persistent_state()
            
            # Start background tasks
            asyncio.create_task(self._state_sync_loop())
            asyncio.create_task(self._cleanup_loop())
            
            self.is_initialized = True
            self.logger.info("State manager initialized")
            return True
            
        except Exception as e:
            self.logger.error(f"State manager initialization failed: {e}")
            return False
    
    async def set_state(self, key: str, value: Any, scope: StateScope = StateScope.USER,
                       access: StateAccess = StateAccess.PROTECTED, owner: str = "system",
                       metadata: Dict[str, Any] = None) -> bool:
        """Set state value with access control"""
        try:
            start_time = datetime.now()
            
            # Validate access permissions
            if not await self._validate_access(owner, key, "write"):
                self.logger.warning(f"Access denied for {owner} to write {key}")
                return False
            
            # Get or create lock for this key
            if key not in self.state_locks:
                self.state_locks[key] = asyncio.Lock()
            
            async with self.state_locks[key]:
                # Create or update state entry
                if key in self.state_store:
                    # Update existing entry
                    entry = self.state_store[key]
                    entry.value = value
                    entry.modified = datetime.now()
                    entry.version += 1
                    if metadata:
                        entry.metadata.update(metadata)
                else:
                    # Create new entry
                    entry = StateEntry(
                        key=key,
                        value=value,
                        scope=scope,
                        access=access,
                        owner=owner,
                        created=datetime.now(),
                        modified=datetime.now(),
                        version=1,
                        metadata=metadata or {}
                    )
                
                self.state_store[key] = entry
                
                # Update component state if applicable
                await self._update_component_state(key, value, scope, owner)
                
                # Notify listeners
                await self._notify_change_listeners(key, value, "set")
                
                # Log access
                await self._log_access(owner, key, "write", True)
            
            # Update metrics
            operation_time = (datetime.now() - start_time).total_seconds()
            await self._update_metrics("write", operation_time)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Set state failed for {key}: {e}")
            await self._log_access(owner, key, "write", False)
            return False
    
    async def get_state(self, key: str, requester: str = "system", 
                       default: Any = None) -> Any:
        """Get state value with access control"""
        try:
            start_time = datetime.now()
            
            # Check if key exists
            if key not in self.state_store:
                await self._update_metrics("read", 0, cache_miss=True)
                return default
            
            entry = self.state_store[key]
            
            # Validate access permissions
            if not await self._validate_access(requester, key, "read"):
                self.logger.warning(f"Access denied for {requester} to read {key}")
                await self._log_access(requester, key, "read", False)
                return default
            
            # Log access
            await self._log_access(requester, key, "read", True)
            
            # Update metrics
            operation_time = (datetime.now() - start_time).total_seconds()
            await self._update_metrics("read", operation_time, cache_hit=True)
            
            return entry.value
            
        except Exception as e:
            self.logger.error(f"Get state failed for {key}: {e}")
            await self._update_metrics("read", 0, cache_miss=True)
            return default
    
    async def delete_state(self, key: str, requester: str = "system") -> bool:
        """Delete state value with access control"""
        try:
            # Validate access permissions
            if not await self._validate_access(requester, key, "delete"):
                self.logger.warning(f"Access denied for {requester} to delete {key}")
                return False
            
            if key in self.state_store:
                # Get lock and delete
                if key in self.state_locks:
                    async with self.state_locks[key]:
                        del self.state_store[key]
                else:
                    del self.state_store[key]
                
                # Notify listeners
                await self._notify_change_listeners(key, None, "delete")
                
                # Log access
                await self._log_access(requester, key, "delete", True)
                
                return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Delete state failed for {key}: {e}")
            await self._log_access(requester, key, "delete", False)
            return False
    
    async def get_component_state(self, component: str, requester: str = "system") -> Dict[str, Any]:
        """Get all state for a specific component"""
        try:
            # Validate component access
            if not await self._validate_component_access(requester, component):
                return {}
            
            return self.component_states.get(component, {}).copy()
            
        except Exception as e:
            self.logger.error(f"Get component state failed for {component}: {e}")
            return {}
    
    async def set_component_state(self, component: str, state_data: Dict[str, Any], 
                                 requester: str = "system") -> bool:
        """Set state for a specific component"""
        try:
            # Validate component access
            if not await self._validate_component_access(requester, component):
                return False
            
            if component not in self.component_states:
                self.component_states[component] = {}
            
            self.component_states[component].update(state_data)
            
            # Also update individual state entries
            for key, value in state_data.items():
                component_key = f"{component}.{key}"
                await self.set_state(
                    component_key, value, 
                    scope=StateScope.COMPONENT, 
                    owner=component
                )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Set component state failed for {component}: {e}")
            return False
    
    async def get_user_state(self, requester: str = "system") -> Dict[str, Any]:
        """Get all user-scoped state"""
        try:
            user_state = {}
            
            for key, entry in self.state_store.items():
                if (entry.scope == StateScope.USER and 
                    await self._validate_access(requester, key, "read")):
                    user_state[key] = entry.value
            
            return user_state
            
        except Exception as e:
            self.logger.error(f"Get user state failed: {e}")
            return {}
    
    async def get_session_state(self, session_id: str = None) -> Dict[str, Any]:
        """Get session-specific state"""
        try:
            if session_id:
                return self.session_data.get(session_id, {}).copy()
            else:
                return self.session_data.copy()
                
        except Exception as e:
            self.logger.error(f"Get session state failed: {e}")
            return {}
    
    async def set_session_state(self, session_id: str, state_data: Dict[str, Any]) -> bool:
        """Set session-specific state"""
        try:
            if session_id not in self.session_data:
                self.session_data[session_id] = {}
            
            self.session_data[session_id].update(state_data)
            
            # Also create state entries
            for key, value in state_data.items():
                session_key = f"session.{session_id}.{key}"
                await self.set_state(
                    session_key, value,
                    scope=StateScope.SESSION,
                    access=StateAccess.PROTECTED
                )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Set session state failed: {e}")
            return False
    
    async def register_change_listener(self, key_pattern: str, callback: callable, 
                                     component: str = "system"):
        """Register a callback for state changes"""
        try:
            if key_pattern not in self.change_listeners:
                self.change_listeners[key_pattern] = []
            
            self.change_listeners[key_pattern].append({
                "callback": callback,
                "component": component,
                "registered": datetime.now()
            })
            
            self.logger.info(f"Change listener registered for {key_pattern} by {component}")
            
        except Exception as e:
            self.logger.error(f"Failed to register change listener: {e}")
    
    async def sync_component_states(self) -> bool:
        """Synchronize state across all components"""
        try:
            # Add sync request to queue
            sync_request = {
                "type": "full_sync",
                "timestamp": datetime.now(),
                "components": list(self.component_states.keys())
            }
            
            self.sync_queue.append(sync_request)
            
            return True
            
        except Exception as e:
            self.logger.error(f"State sync failed: {e}")
            return False
    
    async def get_state_summary(self) -> Dict[str, Any]:
        """Get summary of current state"""
        try:
            summary = {
                "total_entries": len(self.state_store),
                "by_scope": {},
                "by_access": {},
                "by_component": {},
                "performance_metrics": self.performance_metrics.copy(),
                "last_updated": datetime.now().isoformat()
            }
            
            # Count by scope
            for entry in self.state_store.values():
                scope = entry.scope.value
                summary["by_scope"][scope] = summary["by_scope"].get(scope, 0) + 1
                
                access = entry.access.value
                summary["by_access"][access] = summary["by_access"].get(access, 0) + 1
                
                owner = entry.owner
                summary["by_component"][owner] = summary["by_component"].get(owner, 0) + 1
            
            return summary
            
        except Exception as e:
            self.logger.error(f"Get state summary failed: {e}")
            return {}
    
    async def _setup_component_permissions(self):
        """Set up component access permissions"""
        # Default permissions for each component
        self.component_permissions = {
            "rrt_advocate": [
                "crisis.*", "user.stress_level", "user.crisis_history",
                "component.rrt_advocate.*", "session.*"
            ],
            "toi_otoi_framework": [
                "user.preferences.*", "user.optimization.*", "user.learning.*",
                "component.toi_otoi_framework.*", "session.*"
            ],
            "voice_interface": [
                "user.voice_preferences.*", "user.conversation_history",
                "component.voice_interface.*", "session.*"
            ],
            "supervisor_ai": [
                "*"  # Supervisor has access to everything
            ],
            "system": [
                "*"  # System has full access
            ]
        }
        
        self.logger.info("Component permissions configured")
    
    async def _initialize_state_storage(self):
        """Initialize state storage structures"""
        # Initialize component states
        for component in self.component_permissions.keys():
            if component not in ["system"]:
                self.component_states[component] = {}
        
        # Initialize global state
        self.global_state = {
            "system_version": "1.0.0",
            "initialization_time": datetime.now().isoformat(),
            "user_id": self.user_id
        }
        
        self.logger.info("State storage initialized")
    
    async def _load_persistent_state(self):
        """Load state from persistent storage"""
        try:
            # TODO: Implement persistent storage loading
            # For now, just log that we would load from storage
            self.logger.info("Persistent state loading (placeholder)")
            
        except Exception as e:
            self.logger.error(f"Failed to load persistent state: {e}")
    
    async def _validate_access(self, requester: str, key: str, operation: str) -> bool:
        """Validate access permissions for a state operation"""
        try:
            # System always has access
            if requester == "system":
                return True
            
            # Check if requester has permissions
            if requester not in self.component_permissions:
                return False
            
            permissions = self.component_permissions[requester]
            
            # Check for wildcard permission
            if "*" in permissions:
                return True
            
            # Check for specific key permission
            if key in permissions:
                return True
            
            # Check for pattern matching
            for permission in permissions:
                if permission.endswith("*"):
                    pattern = permission[:-1]
                    if key.startswith(pattern):
                        return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Access validation failed: {e}")
            return False
    
    async def _validate_component_access(self, requester: str, component: str) -> bool:
        """Validate access to component state"""
        # Component can always access its own state
        if requester == component:
            return True
        
        # System and supervisor have access to all components
        if requester in ["system", "supervisor_ai"]:
            return True
        
        return False
    
    async def _update_component_state(self, key: str, value: Any, scope: StateScope, owner: str):
        """Update component-specific state"""
        if scope == StateScope.COMPONENT and owner in self.component_states:
            # Extract component key (remove component prefix)
            if "." in key:
                component_key = key.split(".", 1)[1]
                self.component_states[owner][component_key] = value
    
    async def _notify_change_listeners(self, key: str, value: Any, operation: str):
        """Notify registered change listeners"""
        try:
            for pattern, listeners in self.change_listeners.items():
                # Check if key matches pattern
                if self._key_matches_pattern(key, pattern):
                    for listener_info in listeners:
                        try:
                            callback = listener_info["callback"]
                            await callback(key, value, operation)
                        except Exception as e:
                            self.logger.error(f"Change listener callback failed: {e}")
                            
        except Exception as e:
            self.logger.error(f"Change notification failed: {e}")
    
    def _key_matches_pattern(self, key: str, pattern: str) -> bool:
        """Check if key matches pattern"""
        if pattern == "*":
            return True
        
        if pattern.endswith("*"):
            return key.startswith(pattern[:-1])
        
        return key == pattern
    
    async def _log_access(self, requester: str, key: str, operation: str, success: bool):
        """Log state access for audit purposes"""
        access_entry = {
            "timestamp": datetime.now().isoformat(),
            "requester": requester,
            "key": key,
            "operation": operation,
            "success": success
        }
        
        self.access_log.append(access_entry)
        
        # Keep only recent access logs (last 1000)
        if len(self.access_log) > 1000:
            self.access_log = self.access_log[-1000:]
    
    async def _update_metrics(self, operation_type: str, operation_time: float, 
                            cache_hit: bool = False, cache_miss: bool = False):
        """Update performance metrics"""
        self.performance_metrics["total_operations"] += 1
        
        if operation_type == "read":
            self.performance_metrics["read_operations"] += 1
        elif operation_type == "write":
            self.performance_metrics["write_operations"] += 1
        
        if cache_hit:
            self.performance_metrics["cache_hits"] += 1
        elif cache_miss:
            self.performance_metrics["cache_misses"] += 1
        
        # Update average operation time
        total_ops = self.performance_metrics["total_operations"]
        current_avg = self.performance_metrics["avg_operation_time"]
        new_avg = ((current_avg * (total_ops - 1)) + operation_time) / total_ops
        self.performance_metrics["avg_operation_time"] = new_avg
    
    async def _state_sync_loop(self):
        """Background state synchronization loop"""
        while self.is_initialized:
            try:
                await asyncio.sleep(60)  # Sync every minute
                
                if self.sync_queue:
                    sync_request = self.sync_queue.pop(0)
                    await self._process_sync_request(sync_request)
                
            except Exception as e:
                self.logger.error(f"State sync loop error: {e}")
                await asyncio.sleep(30)
    
    async def _cleanup_loop(self):
        """Background cleanup loop"""
        while self.is_initialized:
            try:
                await asyncio.sleep(3600)  # Cleanup every hour
                
                # Clean up old session data
                await self._cleanup_old_sessions()
                
                # Clean up old access logs
                await self._cleanup_access_logs()
                
            except Exception as e:
                self.logger.error(f"Cleanup loop error: {e}")
                await asyncio.sleep(1800)  # Retry in 30 minutes
    
    async def _process_sync_request(self, sync_request: Dict[str, Any]):
        """Process a state synchronization request"""
        try:
            sync_type = sync_request.get("type", "unknown")
            
            if sync_type == "full_sync":
                # Perform full state synchronization
                await self._perform_full_sync()
            
            self.logger.info(f"Processed sync request: {sync_type}")
            
        except Exception as e:
            self.logger.error(f"Sync request processing failed: {e}")
    
    async def _perform_full_sync(self):
        """Perform full state synchronization"""
        # TODO: Implement full synchronization logic
        self.logger.info("Full state sync performed")
    
    async def _cleanup_old_sessions(self):
        """Clean up old session data"""
        try:
            cutoff_time = datetime.now() - timedelta(hours=24)
            
            # Remove old session entries from state store
            keys_to_remove = []
            for key, entry in self.state_store.items():
                if (entry.scope == StateScope.SESSION and 
                    entry.modified < cutoff_time):
                    keys_to_remove.append(key)
            
            for key in keys_to_remove:
                del self.state_store[key]
            
            if keys_to_remove:
                self.logger.info(f"Cleaned up {len(keys_to_remove)} old session entries")
                
        except Exception as e:
            self.logger.error(f"Session cleanup failed: {e}")
    
    async def _cleanup_access_logs(self):
        """Clean up old access logs"""
        try:
            # Keep only last 24 hours of access logs
            cutoff_time = datetime.now() - timedelta(hours=24)
            
            self.access_log = [
                entry for entry in self.access_log
                if datetime.fromisoformat(entry["timestamp"]) > cutoff_time
            ]
            
            self.logger.info("Access logs cleaned up")
            
        except Exception as e:
            self.logger.error(f"Access log cleanup failed: {e}")
    
    async def shutdown(self):
        """Shutdown state manager"""
        try:
            # Save current state
            await self._save_persistent_state()
            
            # Clear in-memory state
            self.state_store.clear()
            self.component_states.clear()
            self.session_data.clear()
            
            self.is_initialized = False
            self.logger.info("State manager shutdown")
            
        except Exception as e:
            self.logger.error(f"State manager shutdown error: {e}")
    
    async def _save_persistent_state(self):
        """Save state to persistent storage"""
        try:
            # TODO: Implement persistent storage saving
            self.logger.info("Persistent state saving (placeholder)")
            
        except Exception as e:
            self.logger.error(f"Failed to save persistent state: {e}")
