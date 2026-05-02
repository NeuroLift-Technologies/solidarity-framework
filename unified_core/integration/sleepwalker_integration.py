"""
Sleepwalker Protocol Integration Module
Integrates the Sleepwalker Protocol (SWP) with the Agent Solidarity Framework Development Kit (ASFDK)

The Sleepwalker Protocol provides governance for long-term emotional continuity
in human-AI interactions. While RRT Advocate handles acute crisis intervention,
SWP governs sustained emotional safety across extended timeframes.
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
import sys
import os

# Add Sleepwalker to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../sleepwalker'))

try:
    from sleepwalker_protocol import SleepwalkerProtocol, EmotionalState, ConsentLevel
except ImportError:
    # Fallback for development
    class SleepwalkerProtocol:
        def __init__(self, *args, **kwargs):
            pass
    class EmotionalState:
        pass
    class ConsentLevel:
        PASSIVE = "PASSIVE"


class SleepwalkerIntegration:
    """Integration wrapper for Sleepwalker Protocol within the unified foundation"""

    def __init__(self, foundation):
        self.foundation = foundation
        self.user_id = foundation.user_id
        self.swp: Optional[SleepwalkerProtocol] = None
        self.is_initialized = False

        self.logger = logging.getLogger(f"SleepwalkerIntegration-{self.user_id}")

    async def initialize(self) -> bool:
        """Initialize the Sleepwalker Protocol integration"""
        try:
            self.swp = SleepwalkerProtocol(
                privacy_mode="local_only",
                logging_enabled=True
            )

            self.is_initialized = True
            self.logger.info("Sleepwalker Protocol integration initialized")
            return True

        except Exception as e:
            self.logger.error(f"Sleepwalker Protocol integration initialization failed: {e}")
            return False

    async def start(self) -> bool:
        """Start Sleepwalker Protocol monitoring"""
        if not self.is_initialized:
            return False

        try:
            self.logger.info("Sleepwalker Protocol started")
            return True

        except Exception as e:
            self.logger.error(f"Failed to start Sleepwalker Protocol: {e}")
            return False

    async def assess_emotional_state(self, user_input: str,
                                     session_history: Optional[List[Any]] = None) -> Dict[str, Any]:
        """Assess user emotional state through Sleepwalker Protocol"""
        if not self.swp:
            return {"error": "Sleepwalker Protocol not available"}

        try:
            assessment = self.swp.assess_interaction(
                user_input,
                session_history=session_history or []
            )

            # Check if RRTA handoff is needed
            emotional_state = assessment.get("emotional_state")
            if emotional_state and self.swp.requires_rrta_handoff(emotional_state):
                await self._trigger_rrta_handoff(emotional_state)

            return {
                "emotional_state": assessment.get("emotional_state", {}).state_type
                    if hasattr(assessment.get("emotional_state", {}), "state_type") else "unknown",
                "protective_state_active": assessment.get("protective_state_active", False),
                "consent_level": assessment.get("consent_level", ConsentLevel.PASSIVE).name
                    if hasattr(assessment.get("consent_level", ConsentLevel.PASSIVE), "name")
                    else str(assessment.get("consent_level", "PASSIVE")),
                "swp_active": assessment.get("swp_active", True),
                "status": "assessed"
            }

        except Exception as e:
            self.logger.error(f"Emotional state assessment failed: {e}")
            return {"error": str(e)}

    async def generate_response_guidance(self, user_input: str,
                                         detected_state: Optional[Any] = None) -> Dict[str, Any]:
        """Generate response guidance based on emotional state"""
        if not self.swp:
            return {"error": "Sleepwalker Protocol not available"}

        try:
            response = self.swp.generate_response(user_input, detected_state)
            return {
                "response_type": response.get("response_type", "neutral"),
                "guidance": response.get("guidance", "Provide task-focused support"),
                "intervention": response.get("intervention", "none"),
                "status": "guidance_generated"
            }

        except Exception as e:
            self.logger.error(f"Response guidance generation failed: {e}")
            return {"error": str(e)}

    async def _trigger_rrta_handoff(self, emotional_state: Any):
        """Trigger RRTA handoff when crisis is detected"""
        try:
            if hasattr(self.foundation, 'communication'):
                await self.foundation.communication.sleepwalker_to_rrt({
                    "emotional_state": str(emotional_state),
                    "handoff_reason": "crisis_detected",
                    "timestamp": datetime.now().isoformat(),
                    "urgent": True
                })
            self.logger.warning("RRTA handoff triggered from Sleepwalker Protocol")
        except Exception as e:
            self.logger.error(f"Failed to trigger RRTA handoff: {e}")

    async def get_status(self) -> Dict[str, Any]:
        """Get Sleepwalker Protocol status"""
        return {
            "available": self.swp is not None,
            "initialized": self.is_initialized,
            "component": "sleepwalker_protocol"
        }

    async def health_check(self) -> Dict[str, Any]:
        """Perform health check"""
        health = {
            "healthy": True,
            "issues": [],
            "component": "sleepwalker_protocol"
        }

        if not self.is_initialized:
            health["healthy"] = False
            health["issues"].append("Not initialized")

        return health

    async def shutdown(self):
        """Shutdown Sleepwalker Protocol integration"""
        try:
            self.logger.info("Sleepwalker Protocol integration shutdown")
        except Exception as e:
            self.logger.error(f"Shutdown error: {e}")
