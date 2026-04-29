#!/usr/bin/env python3
"""
Agent Solidarity Kit integration tests

Exercises unified core initialization, RRT Advocate wiring, and coordination helpers.
"""

import asyncio
import sys
import os
import logging
from datetime import datetime

# Ensure repo root and rrt-advocate/src are importable when run from any cwd
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_RRT_SRC = os.path.join(_REPO_ROOT, "rrt-advocate", "src")
for _p in (_REPO_ROOT, _RRT_SRC):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("IntegrationTest")

async def run_foundation_initialization():
    """Exercise basic unified core initialization (run via ``python tests/integration_test.py``)."""
    try:
        from unified_core.neurolift_foundation import create_foundation, FoundationMode
        
        logger.info("Testing foundation initialization...")
        
        # Create foundation
        foundation = await create_foundation("test_user_001", FoundationMode.UNIFIED)
        
        # Test basic functionality
        status = await foundation.get_system_status()
        logger.info(f"Foundation status: {status}")
        
        # Test system status
        health = await foundation.health_check()
        logger.info(f"Health check: {health}")
        
        # Shutdown
        await foundation.shutdown()
        
        logger.info("✅ Foundation initialization test passed")
        return True
        
    except Exception as e:
        logger.error(f"❌ Foundation initialization test failed: {e}")
        return False

async def run_rrt_advocate():
    """Exercise RRT Advocate wiring (run via ``python tests/integration_test.py``)."""
    try:
        from rrt_advocate import create_rrt_advocate

        rrt_config = os.path.join(
            _REPO_ROOT, "rrt-advocate", "config", "crisis_thresholds.yaml"
        )
        
        logger.info("Testing RRT Advocate...")
        
        # Create RRT Advocate
        advocate = await create_rrt_advocate("test_user_001", config_path=rrt_config)
        
        # Test status report
        status = await advocate.get_status_report()
        logger.info(f"RRT Advocate status: {status}")
        
        # Test crisis assessment
        assessment = await advocate.assess_current_state()
        logger.info(f"Crisis assessment: {assessment.crisis_level.value}")
        
        # Shutdown
        await advocate.shutdown()
        
        logger.info("✅ RRT Advocate test passed")
        return True
        
    except Exception as e:
        logger.error(f"❌ RRT Advocate test failed: {e}")
        return False

async def run_integration_modules():
    """Exercise integration modules (run via ``python tests/integration_test.py``)."""
    try:
        logger.info("Testing integration modules...")
        
        # Test RRT integration
        from unified_core.integration.rrt_integration import RRTAdvocateIntegration
        from unified_core.neurolift_foundation import FoundationConfig, FoundationMode
        
        config = FoundationConfig(user_id="test_user", mode=FoundationMode.UNIFIED)
        foundation = type('MockFoundation', (), {'user_id': 'test_user', 'supervisor': None})()
        
        rrt_integration = RRTAdvocateIntegration(foundation)
        initialized = await rrt_integration.initialize()
        logger.info(f"RRT Integration initialized: {initialized}")
        
        # Test TOI-OTOI integration
        from unified_core.integration.toi_otoi_integration import TOIOTOIIntegration
        
        toi_integration = TOIOTOIIntegration(foundation)
        initialized = await toi_integration.initialize()
        logger.info(f"TOI-OTOI Integration initialized: {initialized}")
        
        logger.info("✅ Integration modules test passed")
        return True
        
    except Exception as e:
        logger.error(f"❌ Integration modules test failed: {e}")
        return False

async def run_state_manager():
    """Exercise state manager (run via ``python tests/integration_test.py``)."""
    try:
        from unified_core.core_coordination.state_manager import UnifiedStateManager, StateScope, StateAccess
        
        logger.info("Testing state manager...")
        
        # Create state manager
        state_manager = UnifiedStateManager("test_user")
        await state_manager.initialize()
        
        # Test setting and getting state
        await state_manager.set_state("test_key", "test_value", StateScope.USER, StateAccess.PROTECTED, "system")
        value = await state_manager.get_state("test_key", "system")
        
        assert value == "test_value", f"Expected 'test_value', got {value}"
        
        # Test state summary
        summary = await state_manager.get_state_summary()
        logger.info(f"State summary: {summary}")
        
        # Shutdown
        await state_manager.shutdown()
        
        logger.info("✅ State manager test passed")
        return True
        
    except Exception as e:
        logger.error(f"❌ State manager test failed: {e}")
        return False

async def main():
    """Run all integration tests"""
    logger.info("=" * 60)
    logger.info("Agent Solidarity Kit integration tests")
    logger.info("=" * 60)
    
    tests = [
        ("Foundation Initialization", run_foundation_initialization),
        ("RRT Advocate", run_rrt_advocate),
        ("Integration Modules", run_integration_modules),
        ("State Manager", run_state_manager),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        logger.info(f"\n--- Running {test_name} Test ---")
        try:
            result = await test_func()
            results.append((test_name, result))
        except Exception as e:
            logger.error(f"Test {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("TEST SUMMARY")
    logger.info("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        logger.info(f"{test_name}: {status}")
        if result:
            passed += 1
    
    logger.info(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        logger.info("🎉 All tests passed! The Agent Solidarity Kit unified core looks healthy.")
        return 0
    else:
        logger.warning(f"⚠️  {total - passed} tests failed. Please review the issues above.")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)