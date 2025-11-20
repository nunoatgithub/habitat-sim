#!/usr/bin/env python3
"""
Example usage of habitat_sim_api package.

This demonstrates how to use the interface-only package for type checking,
API exploration, and development without requiring the full habitat-sim installation.
"""


def example_basic_usage():
    """Example 1: Basic import and usage."""
    print("=" * 60)
    print("Example 1: Basic Import and Usage")
    print("=" * 60)
    
    import habitat_sim_api as habitat_sim
    
    # You can import and reference all classes
    print(f"Package version: {habitat_sim.__version__}")
    print(f"Available modules: {len([x for x in dir(habitat_sim) if not x.startswith('_')])}")
    
    # Create configuration objects (they work until you try to use them)
    config = habitat_sim.Configuration(
        sim_cfg=habitat_sim.SimulatorConfiguration(),
        agents=[]
    )
    print(f"✓ Created Configuration object")
    
    # But trying to create a simulator will raise NotImplementedError
    try:
        sim = habitat_sim.Simulator(config)
    except NotImplementedError as e:
        print(f"✓ Simulator creation raises NotImplementedError (expected)")
    
    print()


def example_type_checking():
    """Example 2: Using for type checking."""
    print("=" * 60)
    print("Example 2: Type Checking with TYPE_CHECKING")
    print("=" * 60)
    
    from typing import TYPE_CHECKING
    
    if TYPE_CHECKING:
        # This import only happens during type checking, not at runtime
        import habitat_sim_api as habitat_sim
    
    def setup_agent(config: "habitat_sim.AgentConfiguration") -> None:
        """
        Function with type hints using habitat_sim types.
        
        IDEs and type checkers can validate the types without needing
        the full habitat-sim installation.
        """
        print(f"Setting up agent with height: {config.height}")
        print(f"Agent radius: {config.radius}")
    
    # Use it
    from habitat_sim_api import AgentConfiguration
    agent_cfg = AgentConfiguration(height=1.8, radius=0.15)
    setup_agent(agent_cfg)
    
    print("✓ Type checking works with IDE autocomplete!")
    print()


def example_api_exploration():
    """Example 3: API exploration."""
    print("=" * 60)
    print("Example 3: API Exploration")
    print("=" * 60)
    
    import habitat_sim_api as habitat_sim
    import inspect
    
    # Explore available sensor types
    print("Available SensorTypes:")
    for attr in dir(habitat_sim.SensorType):
        if not attr.startswith('_'):
            value = getattr(habitat_sim.SensorType, attr)
            print(f"  - {attr}: {value}")
    
    print()
    
    # Check what methods a Simulator has
    print("Simulator methods:")
    for name, method in inspect.getmembers(habitat_sim.Simulator, predicate=inspect.isfunction):
        if not name.startswith('_'):
            sig = inspect.signature(method)
            print(f"  - {name}{sig}")
    
    print()


def example_stubbing_tests():
    """Example 4: Writing tests with stubs."""
    print("=" * 60)
    print("Example 4: Writing Tests with Stubs")
    print("=" * 60)
    
    from habitat_sim_api import Agent, AgentState, ActionSpec
    import habitat_sim_api as habitat_sim
    
    # You can write unit tests that use the API without needing the simulator
    def test_agent_configuration():
        """Test that agent configuration works."""
        config = habitat_sim.AgentConfiguration(
            height=1.5,
            radius=0.1,
        )
        
        # Validate configuration
        assert config.height == 1.5
        assert config.radius == 0.1
        print("✓ Agent configuration test passed")
        
        # You can add actions to the action space
        config.action_space = {
            "move_forward": ActionSpec("move_forward"),
            "turn_left": ActionSpec("turn_left"),
        }
        assert "move_forward" in config.action_space
        print("✓ Action space test passed")
    
    test_agent_configuration()
    print()


def example_documentation():
    """Example 5: Using for documentation."""
    print("=" * 60)
    print("Example 5: Documentation Generation")
    print("=" * 60)
    
    from habitat_sim_api import Simulator, Configuration
    
    # All classes have docstrings
    print("Simulator class documentation:")
    print(Simulator.__doc__)
    print()
    
    print("Configuration class documentation:")
    print(Configuration.__doc__)
    print()


def main():
    """Run all examples."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "habitat_sim_api Usage Examples" + " " * 17 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    examples = [
        example_basic_usage,
        example_type_checking,
        example_api_exploration,
        example_stubbing_tests,
        example_documentation,
    ]
    
    for example in examples:
        example()
    
    print("=" * 60)
    print("Examples complete!")
    print("=" * 60)
    print()
    print("Key Takeaways:")
    print("  • habitat_sim_api provides the complete API surface")
    print("  • Use it for type checking, IDE autocomplete, and tests")
    print("  • All execution raises NotImplementedError")
    print("  • For actual simulation, use the real habitat-sim")
    print()


if __name__ == "__main__":
    main()
