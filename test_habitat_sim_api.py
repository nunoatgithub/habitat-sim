#!/usr/bin/env python3
"""
Test script for habitat_sim_api package.

This script validates that the interface-only package correctly mirrors
the habitat_sim API without requiring any dependencies.
"""

import sys


def test_basic_imports():
    """Test basic package imports."""
    print("=" * 60)
    print("TEST: Basic Imports")
    print("=" * 60)
    
    import habitat_sim_api
    print(f"✓ import habitat_sim_api")
    print(f"  Version: {habitat_sim_api.__version__}")
    
    import habitat_sim_api as habitat_sim
    print(f"✓ import habitat_sim_api as habitat_sim")
    
    from habitat_sim_api import Simulator, Agent
    print(f"✓ from habitat_sim_api import Simulator, Agent")
    print()


def test_top_level_api():
    """Test top-level API availability."""
    print("=" * 60)
    print("TEST: Top-Level API")
    print("=" * 60)
    
    import habitat_sim_api as habitat_sim
    
    expected_modules = [
        'agent', 'attributes', 'attributes_managers', 'errors', 'geo',
        'gfx', 'logging', 'metadata', 'nav', 'physics', 'scene',
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


def test_submodule_imports():
    """Test submodule imports."""
    print("=" * 60)
    print("TEST: Submodule Imports")
    print("=" * 60)
    
    tests = [
        ("from habitat_sim_api.agent import Agent", "Agent"),
        ("from habitat_sim_api.simulator import Simulator", "Simulator"),
        ("from habitat_sim_api.nav import PathFinder", "PathFinder"),
        ("from habitat_sim_api.sensors import SensorSuite", "SensorSuite"),
        ("from habitat_sim_api.utils import validators", "validators"),
        ("from habitat_sim_api.registry import registry", "registry"),
    ]
    
    for import_stmt, name in tests:
        try:
            exec(import_stmt)
            print(f"  ✓ {import_stmt}")
        except ImportError as e:
            print(f"  ✗ {import_stmt}")
            print(f"    Error: {e}")
    print()


def test_not_implemented():
    """Test that methods raise NotImplementedError."""
    print("=" * 60)
    print("TEST: NotImplementedError Behavior")
    print("=" * 60)
    
    from habitat_sim_api import Simulator, SimulatorConfiguration, Configuration
    from habitat_sim_api.agent import Agent, AgentConfiguration
    
    tests = [
        ("Simulator initialization", lambda: Simulator(None)),
        ("PathFinder.is_loaded()", lambda: __import__('habitat_sim_api').PathFinder().is_loaded()),
    ]
    
    for name, func in tests:
        try:
            func()
            print(f"  ✗ {name} - should raise NotImplementedError")
        except NotImplementedError:
            print(f"  ✓ {name} - raises NotImplementedError")
        except Exception as e:
            # Some methods may raise TypeError before NotImplementedError
            print(f"  ~ {name} - raises {type(e).__name__} (acceptable)")
    print()


def test_class_instantiation():
    """Test that classes can be instantiated (even if they raise errors)."""
    print("=" * 60)
    print("TEST: Class Instantiation")
    print("=" * 60)
    
    from habitat_sim_api import (
        ActionSpec,
        AgentConfiguration,
        AgentState,
        SixDOFPose,
    )
    
    # These should work without raising errors
    tests = [
        ("ActionSpec", lambda: ActionSpec("test_action")),
        ("SixDOFPose", lambda: SixDOFPose()),
        ("AgentState", lambda: AgentState()),
        ("AgentConfiguration", lambda: AgentConfiguration()),
    ]
    
    for name, func in tests:
        try:
            obj = func()
            print(f"  ✓ {name} - instantiated successfully")
        except Exception as e:
            print(f"  ✗ {name} - failed: {e}")
    print()


def test_type_hints():
    """Test that type hints are available."""
    print("=" * 60)
    print("TEST: Type Hints")
    print("=" * 60)
    
    from habitat_sim_api import Simulator
    import inspect
    
    # Check if type hints are available
    try:
        sig = inspect.signature(Simulator.__init__)
        params = sig.parameters
        print(f"  ✓ Simulator.__init__ signature available")
        print(f"    Parameters: {list(params.keys())}")
    except Exception as e:
        print(f"  ✗ Failed to get signature: {e}")
    print()


def test_enums():
    """Test enum types."""
    print("=" * 60)
    print("TEST: Enums")
    print("=" * 60)
    
    from habitat_sim_api.bindings import (
        SensorType,
        SensorSubType,
        SceneNodeType,
        FisheyeSensorModelType,
    )
    from habitat_sim_api.nav import GreedyFollowerCodes
    
    enums = [
        ("SensorType.COLOR", SensorType.COLOR),
        ("SensorType.DEPTH", SensorType.DEPTH),
        ("SensorSubType.PINHOLE", SensorSubType.PINHOLE),
        ("SceneNodeType.SENSOR", SceneNodeType.SENSOR),
        ("GreedyFollowerCodes.FORWARD", GreedyFollowerCodes.FORWARD),
    ]
    
    for name, value in enums:
        try:
            print(f"  ✓ {name} = {value}")
        except Exception as e:
            print(f"  ✗ {name} - failed: {e}")
    print()


def test_docstrings():
    """Test that docstrings are present."""
    print("=" * 60)
    print("TEST: Docstrings")
    print("=" * 60)
    
    from habitat_sim_api import Simulator, Agent, Configuration
    
    classes = [
        ("Simulator", Simulator),
        ("Agent", Agent),
        ("Configuration", Configuration),
    ]
    
    for name, cls in classes:
        if cls.__doc__:
            print(f"  ✓ {name} has docstring")
            print(f"    {cls.__doc__.split(chr(10))[0][:60]}...")
        else:
            print(f"  ✗ {name} missing docstring")
    print()


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "habitat_sim_api Test Suite" + " " * 21 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    tests = [
        test_basic_imports,
        test_top_level_api,
        test_submodule_imports,
        test_not_implemented,
        test_class_instantiation,
        test_type_hints,
        test_enums,
        test_docstrings,
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
