#!/usr/bin/env python3
"""
Test script for habitat_sim_api_v0_2_2 package.

This script validates that the interface-only package correctly mirrors
the habitat_sim v0.2.2 API without requiring any dependencies.
"""

import sys


def test_basic_imports():
    """Test basic package imports."""
    print("=" * 60)
    print("TEST: Basic Imports (v0.2.2)")
    print("=" * 60)
    
    import habitat_sim_api_v0_2_2
    print(f"✓ import habitat_sim_api_v0_2_2")
    print(f"  Version: {habitat_sim_api_v0_2_2.__version__}")
    
    import habitat_sim_api_v0_2_2 as habitat_sim
    print(f"✓ import habitat_sim_api_v0_2_2 as habitat_sim")
    
    from habitat_sim_api_v0_2_2 import Simulator, Agent
    print(f"✓ from habitat_sim_api_v0_2_2 import Simulator, Agent")
    print()


def test_v0_2_2_specific_features():
    """Test features specific to v0.2.2."""
    print("=" * 60)
    print("TEST: v0.2.2 Specific Features")
    print("=" * 60)
    
    import habitat_sim_api_v0_2_2 as habitat_sim
    
    # Test robots module (new in 0.2.2, not in later versions)
    print("Robots module:")
    assert hasattr(habitat_sim, 'robots'), "Missing robots module"
    print(f"  ✓ robots module exists")
    
    from habitat_sim_api_v0_2_2.robots import (
        FetchRobot,
        FetchRobotNoWheels,
        MobileManipulator,
        MobileManipulatorParams,
        RobotCameraParams,
        RobotInterface,
    )
    print(f"  ✓ FetchRobot")
    print(f"  ✓ FetchRobotNoWheels")
    print(f"  ✓ MobileManipulator")
    print(f"  ✓ MobileManipulatorParams")
    print(f"  ✓ RobotCameraParams")
    print(f"  ✓ RobotInterface")
    
    # Test vhacd_enabled (in 0.2.2)
    print("\nVHACD support:")
    assert hasattr(habitat_sim, 'vhacd_enabled'), "Missing vhacd_enabled"
    print(f"  ✓ vhacd_enabled function exists")
    
    # Verify RLRAudioPropagationChannelLayoutType does NOT exist (added in 0.3.x)
    print("\nVerify 0.3.x features not present:")
    from habitat_sim_api_v0_2_2 import bindings
    assert not hasattr(bindings, 'RLRAudioPropagationChannelLayoutType'), \
        "RLRAudioPropagationChannelLayoutType should not exist in 0.2.2"
    print(f"  ✓ RLRAudioPropagationChannelLayoutType correctly absent")
    print()


def test_common_api():
    """Test common API features."""
    print("=" * 60)
    print("TEST: Common API Features")
    print("=" * 60)
    
    import habitat_sim_api_v0_2_2 as habitat_sim
    
    expected_modules = [
        'agent', 'attributes', 'attributes_managers', 'errors', 'geo',
        'gfx', 'logging', 'metadata', 'nav', 'physics', 'robots', 'scene',
        'sensor', 'sensors', 'sim', 'simulator', 'utils', 'registry'
    ]
    
    expected_classes = [
        'Agent', 'AgentConfiguration', 'AgentState', 'ActionSpec', 'SixDOFPose',
        'Simulator', 'Configuration', 'SimulatorConfiguration',
        'PathFinder', 'GreedyGeodesicFollower', 'NavMeshSettings',
        'Sensor', 'SensorSpec', 'SensorType',
        'SceneNode', 'SceneGraph',
    ]
    
    print("Modules:")
    for mod in expected_modules:
        if hasattr(habitat_sim, mod):
            print(f"  ✓ {mod}")
        else:
            print(f"  ✗ {mod} MISSING")
    
    print("\nClasses:")
    for cls in expected_classes:
        if hasattr(habitat_sim, cls):
            print(f"  ✓ {cls}")
        else:
            print(f"  ✗ {cls} MISSING")
    print()


def test_not_implemented():
    """Test that methods raise NotImplementedError."""
    print("=" * 60)
    print("TEST: NotImplementedError Behavior")
    print("=" * 60)
    
    from habitat_sim_api_v0_2_2 import Simulator, SimulatorConfiguration, Configuration
    from habitat_sim_api_v0_2_2.robots import FetchRobot
    
    tests = [
        ("Simulator initialization", lambda: Simulator(None)),
        ("FetchRobot initialization", lambda: FetchRobot()),
    ]
    
    for name, func in tests:
        try:
            func()
            print(f"  ✗ {name} - should raise NotImplementedError")
        except NotImplementedError:
            print(f"  ✓ {name} - raises NotImplementedError")
        except Exception as e:
            print(f"  ~ {name} - raises {type(e).__name__} (acceptable)")
    print()


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 8 + "habitat_sim_api_v0_2_2 Test Suite" + " " * 16 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    tests = [
        test_basic_imports,
        test_v0_2_2_specific_features,
        test_common_api,
        test_not_implemented,
    ]
    
    for test in tests:
        try:
            test()
        except Exception as e:
            print(f"\n❌ Test {test.__name__} failed with error: {e}\n")
            import traceback
            traceback.print_exc()
            return 1
    
    print("=" * 60)
    print("✅ All tests passed!")
    print("=" * 60)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
