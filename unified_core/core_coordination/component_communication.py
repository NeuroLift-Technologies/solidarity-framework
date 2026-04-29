"""
Component Communication - Inter-component coordination for the Agent Solidarity Framework Development Kit (ASFDK)
Manages communication and data flow between all foundation components
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass
from enum import Enum

class MessageType(Enum):
    """Types of inter-component messages"""
    STATUS_UPDATE = "status_update"
    CRISIS_ALERT = "crisis_alert"
    OPTIMIZATION_REQUEST = "optimization_request"
    VOICE_ANALYSIS = "voice_analysis"
    PREFERENCE_UPDATE = "preference_update"
    COORDINATION_REQUEST = "coordination_request"
    HEALTH_CHECK = "health_check"
    EMERGENCY = "emergency"

class MessagePriority(Enum):
    """Message priority levels"""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    URGENT = 4
    EMERGENCY = 5

@dataclass
class ComponentMessage:
    """Message between components"""
    id: str
    timestamp: datetime
    source: str
    destination: str
    message_type: MessageType
    priority: MessagePriority
    data: Dict[str, Any]
    callback: Optional[Callable] = None
    processed: bool = False

class ComponentCommunication:
    """
    Manages communication between all Agent Solidarity Framework Development Kit (ASFDK) components
    
    Provides a centralized communication hub for RRT Advocate, TOI-OTOI Framework,
    Voice Interface, and Supervisor AI to coordinate their activities.
    """
    
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.is_active = False
        
        # Communication channels
        self.message_queue: List[ComponentMessage] = []
        self.active_channels: Dict[str, Dict[str, Any]] = {}
        self.message_handlers: Dict[str, Dict[MessageType, Callable]] = {}
        
        # Performance tracking
        self.communication_metrics = {
            "total_messages": 0,
            "messages_by_type": {},
            "avg_processing_time": 0.0,
            "failed_messages": 0,
            "active_channels": 0
        }
        
        self.logger = logging.getLogger("ComponentCommunication")
        
    async def initialize(self) -> bool:
        """Initialize component communication system"""
        try:
            # Set up message processing
            await self._setup_message_processing()
            
            # Initialize communication channels
            await self._initialize_channels()
            
            self.is_active = True
            self.logger.info("Component communication initialized")
            return True
            
        except Exception as e:
            self.logger.error(f"Communication initialization failed: {e}")
            return False
    
    async def link_rrt_voice(self, rrt_component, voice_component):
        """Establish communication link between RRT Advocate and Voice Interface"""
        try:
            channel_id = "rrt_voice_channel"
            
            # Set up bidirectional communication
            self.active_channels[channel_id] = {
                "components": ["rrt_advocate", "voice_interface"],
                "rrt_instance": rrt_component,
                "voice_instance": voice_component,
                "established": datetime.now(),
                "message_count": 0
            }
            
            # Register message handlers
            await self._register_rrt_voice_handlers(rrt_component, voice_component)
            
            self.logger.info("RRT-Voice communication link established")
            
        except Exception as e:
            self.logger.error(f"Failed to link RRT-Voice: {e}")

    async def link_rrt_sleepwalker(self, rrt_component, sleepwalker_component):
        """Backward-compatible alias for linking RRT Advocate and Sleepwalker."""
        try:
            channel_id = "rrt_sleepwalker_channel"
            self.active_channels[channel_id] = {
                "components": ["rrt_advocate", "sleepwalker_protocol"],
                "rrt_instance": rrt_component,
                "sleepwalker_instance": sleepwalker_component,
                "established": datetime.now(),
                "message_count": 0
            }
            self.logger.info("RRT-Sleepwalker communication link established")
        except Exception as e:
            self.logger.error(f"Failed to link RRT-Sleepwalker: {e}")
    
    async def link_voice_framework(self, voice_component, framework_component):
        """Establish communication link between Voice Interface and TOI-OTOI Framework"""
        try:
            channel_id = "voice_framework_channel"
            
            self.active_channels[channel_id] = {
                "components": ["voice_interface", "toi_otoi_framework"],
                "voice_instance": voice_component,
                "framework_instance": framework_component,
                "established": datetime.now(),
                "message_count": 0
            }
            
            await self._register_voice_framework_handlers(voice_component, framework_component)
            
            self.logger.info("Voice-Framework communication link established")
            
        except Exception as e:
            self.logger.error(f"Failed to link Voice-Framework: {e}")

    async def link_sleepwalker_framework(self, sleepwalker_component, framework_component):
        """Backward-compatible alias for linking Sleepwalker and Framework."""
        try:
            channel_id = "sleepwalker_framework_channel"
            self.active_channels[channel_id] = {
                "components": ["sleepwalker_protocol", "toi_otoi_framework"],
                "sleepwalker_instance": sleepwalker_component,
                "framework_instance": framework_component,
                "established": datetime.now(),
                "message_count": 0
            }
            self.logger.info("Sleepwalker-Framework communication link established")
        except Exception as e:
            self.logger.error(f"Failed to link Sleepwalker-Framework: {e}")
    
    async def link_framework_rrt(self, framework_component, rrt_component):
        """Establish communication link between TOI-OTOI Framework and RRT Advocate"""
        try:
            channel_id = "framework_rrt_channel"
            
            self.active_channels[channel_id] = {
                "components": ["toi_otoi_framework", "rrt_advocate"],
                "framework_instance": framework_component,
                "rrt_instance": rrt_component,
                "established": datetime.now(),
                "message_count": 0
            }
            
            await self._register_framework_rrt_handlers(framework_component, rrt_component)
            
            self.logger.info("Framework-RRT communication link established")
            
        except Exception as e:
            self.logger.error(f"Failed to link Framework-RRT: {e}")
    
    async def link_supervisor(self, supervisor_component, components: List[Any]):
        """Establish communication links between Supervisor AI and all components"""
        try:
            for component in components:
                if component:  # Check if component exists
                    component_name = component.__class__.__name__.lower()
                    channel_id = f"supervisor_{component_name}_channel"
                    
                    self.active_channels[channel_id] = {
                        "components": ["supervisor_ai", component_name],
                        "supervisor_instance": supervisor_component,
                        "component_instance": component,
                        "established": datetime.now(),
                        "message_count": 0
                    }
            
            await self._register_supervisor_handlers(supervisor_component, components)
            
            self.logger.info("Supervisor communication links established")
            
        except Exception as e:
            self.logger.error(f"Failed to link Supervisor: {e}")
    
    async def send_message(self, source: str, destination: str, message_type: MessageType, 
                          data: Dict[str, Any], priority: MessagePriority = MessagePriority.NORMAL,
                          callback: Optional[Callable] = None) -> str:
        """Send a message between components"""
        try:
            message_id = f"msg_{datetime.now().timestamp()}"
            
            message = ComponentMessage(
                id=message_id,
                timestamp=datetime.now(),
                source=source,
                destination=destination,
                message_type=message_type,
                priority=priority,
                data=data,
                callback=callback
            )
            
            # Add to queue based on priority
            await self._queue_message(message)
            
            self.communication_metrics["total_messages"] += 1
            
            return message_id
            
        except Exception as e:
            self.logger.error(f"Failed to send message: {e}")
            self.communication_metrics["failed_messages"] += 1
            return ""
    
    async def rrt_to_voice(self, crisis_data: Dict[str, Any]) -> bool:
        """Send crisis data from RRT Advocate to Voice Interface"""
        try:
            return await self.send_message(
                source="rrt_advocate",
                destination="voice_interface",
                message_type=MessageType.CRISIS_ALERT,
                data=crisis_data,
                priority=MessagePriority.HIGH
            ) != ""
            
        except Exception as e:
            self.logger.error(f"RRT to Voice communication failed: {e}")
            return False
    
    async def voice_to_framework(self, voice_data: Dict[str, Any]) -> bool:
        """Send voice analysis data to TOI-OTOI Framework"""
        try:
            return await self.send_message(
                source="voice_interface",
                destination="toi_otoi_framework",
                message_type=MessageType.VOICE_ANALYSIS,
                data=voice_data,
                priority=MessagePriority.NORMAL
            ) != ""
            
        except Exception as e:
            self.logger.error(f"Voice to Framework communication failed: {e}")
            return False
    
    async def framework_to_rrt(self, optimization_data: Dict[str, Any]) -> bool:
        """Send optimization data from Framework to RRT Advocate"""
        try:
            return await self.send_message(
                source="toi_otoi_framework",
                destination="rrt_advocate",
                message_type=MessageType.OPTIMIZATION_REQUEST,
                data=optimization_data,
                priority=MessagePriority.NORMAL
            ) != ""
            
        except Exception as e:
            self.logger.error(f"Framework to RRT communication failed: {e}")
            return False
    
    async def voice_to_rrt(self, stress_data: Dict[str, Any]) -> bool:
        """Send stress detection data from Voice to RRT Advocate"""
        try:
            return await self.send_message(
                source="voice_interface",
                destination="rrt_advocate",
                message_type=MessageType.CRISIS_ALERT,
                data=stress_data,
                priority=MessagePriority.HIGH
            ) != ""
            
        except Exception as e:
            self.logger.error(f"Voice to RRT communication failed: {e}")
            return False
    
    async def broadcast_emergency(self, source: str, emergency_data: Dict[str, Any]) -> List[str]:
        """Broadcast emergency message to all components"""
        try:
            message_ids = []
            
            # Send to all active components except source
            for channel_id, channel_info in self.active_channels.items():
                for component in channel_info["components"]:
                    if component != source:
                        message_id = await self.send_message(
                            source=source,
                            destination=component,
                            message_type=MessageType.EMERGENCY,
                            data=emergency_data,
                            priority=MessagePriority.EMERGENCY
                        )
                        if message_id:
                            message_ids.append(message_id)
            
            return message_ids
            
        except Exception as e:
            self.logger.error(f"Emergency broadcast failed: {e}")
            return []
    
    async def request_coordination(self, requester: str, coordination_data: Dict[str, Any]) -> str:
        """Request coordination from Supervisor AI"""
        try:
            return await self.send_message(
                source=requester,
                destination="supervisor_ai",
                message_type=MessageType.COORDINATION_REQUEST,
                data=coordination_data,
                priority=MessagePriority.HIGH
            )
            
        except Exception as e:
            self.logger.error(f"Coordination request failed: {e}")
            return ""
    
    async def _setup_message_processing(self):
        """Set up message processing system"""
        # Start message processing loop
        asyncio.create_task(self._message_processing_loop())
        
        self.logger.info("Message processing setup complete")
    
    async def _initialize_channels(self):
        """Initialize communication channels"""
        self.communication_metrics["active_channels"] = 0
        
        self.logger.info("Communication channels initialized")
    
    async def _message_processing_loop(self):
        """Main message processing loop"""
        while self.is_active:
            try:
                await asyncio.sleep(0.1)  # Process messages every 100ms
                
                if self.message_queue:
                    # Sort by priority
                    self.message_queue.sort(key=lambda m: m.priority.value, reverse=True)
                    
                    # Process highest priority message
                    message = self.message_queue.pop(0)
                    await self._process_message(message)
                
            except Exception as e:
                self.logger.error(f"Message processing error: {e}")
                await asyncio.sleep(1)
    
    async def _queue_message(self, message: ComponentMessage):
        """Add message to processing queue"""
        self.message_queue.append(message)
        
        # Update metrics
        msg_type = message.message_type.value
        if msg_type not in self.communication_metrics["messages_by_type"]:
            self.communication_metrics["messages_by_type"][msg_type] = 0
        self.communication_metrics["messages_by_type"][msg_type] += 1
    
    async def _process_message(self, message: ComponentMessage):
        """Process a single message"""
        try:
            start_time = datetime.now()
            
            # Find appropriate handler
            handler = await self._get_message_handler(message.destination, message.message_type)
            
            if handler:
                # Process message
                await handler(message)
                message.processed = True
                
                # Execute callback if provided
                if message.callback:
                    await message.callback(message)
            else:
                self.logger.warning(f"No handler for {message.message_type} to {message.destination}")
            
            # Update processing time metrics
            processing_time = (datetime.now() - start_time).total_seconds()
            self._update_processing_time_metrics(processing_time)
            
        except Exception as e:
            self.logger.error(f"Message processing failed: {e}")
            self.communication_metrics["failed_messages"] += 1
    
    async def _get_message_handler(self, destination: str, message_type: MessageType) -> Optional[Callable]:
        """Get appropriate message handler for destination and type"""
        if destination in self.message_handlers:
            return self.message_handlers[destination].get(message_type)
        return None
    
    async def _register_rrt_voice_handlers(self, rrt_component, voice_component):
        """Register message handlers for RRT-Voice communication"""
        # RRT Advocate handlers
        if "rrt_advocate" not in self.message_handlers:
            self.message_handlers["rrt_advocate"] = {}
        
        self.message_handlers["rrt_advocate"][MessageType.VOICE_ANALYSIS] = \
            lambda msg: self._handle_voice_to_rrt(rrt_component, msg)
        
        # Voice Interface handlers
        if "voice_interface" not in self.message_handlers:
            self.message_handlers["voice_interface"] = {}
        
        self.message_handlers["voice_interface"][MessageType.CRISIS_ALERT] = \
            lambda msg: self._handle_rrt_to_voice(voice_component, msg)
    
    async def _register_voice_framework_handlers(self, voice_component, framework_component):
        """Register message handlers for Voice-Framework communication"""
        # Voice Interface handlers
        if "voice_interface" not in self.message_handlers:
            self.message_handlers["voice_interface"] = {}
        
        self.message_handlers["voice_interface"][MessageType.OPTIMIZATION_REQUEST] = \
            lambda msg: self._handle_framework_to_voice(voice_component, msg)
        
        # Framework handlers
        if "toi_otoi_framework" not in self.message_handlers:
            self.message_handlers["toi_otoi_framework"] = {}
        
        self.message_handlers["toi_otoi_framework"][MessageType.VOICE_ANALYSIS] = \
            lambda msg: self._handle_voice_to_framework(framework_component, msg)
    
    async def _register_framework_rrt_handlers(self, framework_component, rrt_component):
        """Register message handlers for Framework-RRT communication"""
        # Framework handlers
        if "toi_otoi_framework" not in self.message_handlers:
            self.message_handlers["toi_otoi_framework"] = {}
        
        self.message_handlers["toi_otoi_framework"][MessageType.CRISIS_ALERT] = \
            lambda msg: self._handle_rrt_to_framework(framework_component, msg)
        
        # RRT Advocate handlers
        if "rrt_advocate" not in self.message_handlers:
            self.message_handlers["rrt_advocate"] = {}
        
        self.message_handlers["rrt_advocate"][MessageType.OPTIMIZATION_REQUEST] = \
            lambda msg: self._handle_framework_to_rrt(rrt_component, msg)
    
    async def _register_supervisor_handlers(self, supervisor_component, components):
        """Register message handlers for Supervisor communication"""
        # Supervisor handlers
        if "supervisor_ai" not in self.message_handlers:
            self.message_handlers["supervisor_ai"] = {}
        
        self.message_handlers["supervisor_ai"][MessageType.COORDINATION_REQUEST] = \
            lambda msg: self._handle_coordination_request(supervisor_component, msg)
        self.message_handlers["supervisor_ai"][MessageType.EMERGENCY] = \
            lambda msg: self._handle_emergency_to_supervisor(supervisor_component, msg)
    
    # Message handling methods
    async def _handle_rrt_to_voice(self, voice_component, message: ComponentMessage):
        """Handle crisis alert from RRT to Voice"""
        try:
            await voice_component.provide_crisis_support(message.data)
            self.logger.info("Crisis alert delivered to Voice Interface")
        except Exception as e:
            self.logger.error(f"RRT to Voice handling failed: {e}")
    
    async def _handle_voice_to_rrt(self, rrt_component, message: ComponentMessage):
        """Handle voice analysis data to RRT"""
        try:
            await rrt_component.handle_crisis(message.data)
            self.logger.info("Voice analysis delivered to RRT Advocate")
        except Exception as e:
            self.logger.error(f"Voice to RRT handling failed: {e}")
    
    async def _handle_voice_to_framework(self, framework_component, message: ComponentMessage):
        """Handle voice data to Framework"""
        try:
            await framework_component.process_voice_configuration(message.data)
            self.logger.info("Voice data delivered to Framework")
        except Exception as e:
            self.logger.error(f"Voice to Framework handling failed: {e}")
    
    async def _handle_framework_to_voice(self, voice_component, message: ComponentMessage):
        """Handle optimization request to Voice"""
        try:
            # Apply voice optimizations
            self.logger.info("Optimization request delivered to Voice Interface")
        except Exception as e:
            self.logger.error(f"Framework to Voice handling failed: {e}")
    
    async def _handle_framework_to_rrt(self, rrt_component, message: ComponentMessage):
        """Handle optimization request to RRT"""
        try:
            # Apply RRT optimizations
            self.logger.info("Optimization request delivered to RRT Advocate")
        except Exception as e:
            self.logger.error(f"Framework to RRT handling failed: {e}")
    
    async def _handle_rrt_to_framework(self, framework_component, message: ComponentMessage):
        """Handle crisis data to Framework"""
        try:
            await framework_component.analyze_interaction_for_optimization(
                message.data.get("interaction"), message.data.get("response")
            )
            self.logger.info("Crisis data delivered to Framework")
        except Exception as e:
            self.logger.error(f"RRT to Framework handling failed: {e}")
    
    async def _handle_coordination_request(self, supervisor_component, message: ComponentMessage):
        """Handle coordination request to Supervisor"""
        try:
            await supervisor_component.coordinate_response(
                message.data.get("interaction_type", "unknown"),
                message.data
            )
            self.logger.info("Coordination request processed by Supervisor")
        except Exception as e:
            self.logger.error(f"Coordination request handling failed: {e}")
    
    async def _handle_emergency_to_supervisor(self, supervisor_component, message: ComponentMessage):
        """Handle emergency message to Supervisor"""
        try:
            await supervisor_component.emergency_escalation(
                message.source,
                message.data.get("crisis_assessment"),
                message.data.get("user_id")
            )
            self.logger.critical("Emergency escalated to Supervisor")
        except Exception as e:
            self.logger.critical(f"Emergency handling failed: {e}")
    
    def _update_processing_time_metrics(self, processing_time: float):
        """Update processing time metrics"""
        total_messages = self.communication_metrics["total_messages"]
        current_avg = self.communication_metrics["avg_processing_time"]
        
        # Calculate new average
        new_avg = ((current_avg * (total_messages - 1)) + processing_time) / total_messages
        self.communication_metrics["avg_processing_time"] = new_avg
    
    async def get_status(self) -> Dict[str, Any]:
        """Get communication system status"""
        return {
            "active": self.is_active,
            "active_channels": len(self.active_channels),
            "message_queue_size": len(self.message_queue),
            "metrics": self.communication_metrics,
            "registered_handlers": {
                component: list(handlers.keys()) 
                for component, handlers in self.message_handlers.items()
            }
        }
    
    async def shutdown(self):
        """Shutdown component communication"""
        try:
            self.is_active = False
            
            # Clear message queue
            self.message_queue.clear()
            
            # Close all channels
            self.active_channels.clear()
            
            self.logger.info("Component communication shutdown")
        except Exception as e:
            self.logger.error(f"Communication shutdown error: {e}")
