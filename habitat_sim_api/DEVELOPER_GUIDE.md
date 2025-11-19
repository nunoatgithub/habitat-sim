# habitat_sim_api - Developer Guide

## Overview

`habitat_sim_api` is a pure-Python, interface-only package that provides the complete API surface of [habitat-sim](https://github.com/facebookresearch/habitat-sim) without any compiled extensions or runtime behavior.

## Installation

### Option 1: Using setup.py (Recommended)

```bash
cd /path/to/habitat-sim
python habitat_sim_api_setup.py install
```

Or for development:
```bash
python habitat_sim_api_setup.py develop
```

### Option 2: Direct import

Simply add the repository to your Python path:
```python
import sys
sys.path.insert(0, '/path/to/habitat-sim')
import habitat_sim_api as habitat_sim
```

## Use Cases

### 1. Type Checking and IDE Support

Use `TYPE_CHECKING` to import the package only during static analysis:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import habitat_sim_api as habitat_sim

def process_observations(
    obs: "habitat_sim.ObservationDict",
    agent: "habitat_sim.Agent"
) -> None:
    # Your IDE provides full autocomplete here!
    pass
```

### 2. API Exploration

Discover what's available in habitat-sim:

```python
import habitat_sim_api as habitat_sim
import inspect

# List all sensor types
for sensor_type in habitat_sim.SensorType:
    print(sensor_type)

# Explore Simulator methods
for name, method in inspect.getmembers(habitat_sim.Simulator):
    if not name.startswith('_') and callable(method):
        print(f"{name}: {inspect.signature(method)}")
```

### 3. Unit Testing Without Dependencies

Write tests that validate API usage without needing the full simulator:

```python
import unittest
from habitat_sim_api import AgentConfiguration, ActionSpec

class TestAgentSetup(unittest.TestCase):
    def test_agent_configuration(self):
        config = AgentConfiguration(
            height=1.5,
            radius=0.1,
        )
        
        # Test configuration logic
        self.assertEqual(config.height, 1.5)
        self.assertEqual(config.radius, 0.1)
        
        # Add actions
        config.action_space = {
            "move_forward": ActionSpec("move_forward"),
        }
        self.assertIn("move_forward", config.action_space)
```

### 4. Documentation Generation

Generate API documentation without compiling C++:

```python
from habitat_sim_api import Simulator
import pydoc

# Generate HTML docs
pydoc.writedoc(Simulator)
```

## Package Structure

```
habitat_sim_api/
├── __init__.py                 # Top-level package
│
├── agent/                      # Agent-related classes
│   ├── agent.py               # Agent, AgentState, AgentConfiguration
│   └── controls/              # Control specifications
│       ├── controls.py        # SceneNodeControl, ActuationSpec
│       ├── default_controls.py
│       ├── object_controls.py
│       └── pyrobot_noisy_controls.py
│
├── bindings.py                # Stubs for C++ bindings
│   # Contains: SceneNode, SceneGraph, Sensor classes, etc.
│
├── simulator.py               # Simulator and Configuration
│
├── nav/                       # Navigation
│   ├── __init__.py           # PathFinder, NavMeshSettings
│   └── greedy_geodesic_follower.py
│
├── sensors/                   # Sensors
│   ├── sensor_suite.py       # SensorSuite
│   └── noise_models/         # Noise model implementations
│
├── utils/                     # Utilities
│   ├── common/               # Common utilities
│   │   ├── common.py         # Quaternion functions
│   │   └── quaternion_utils.py
│   ├── validators.py         # Validation utilities
│   ├── settings.py           # Settings utilities
│   ├── viz_utils.py          # Visualization utilities
│   └── classes/              # Utility classes
│
├── attributes.py              # Attribute classes
├── attributes_managers.py     # Attribute managers
├── errors.py                  # Custom exceptions
├── geo.py                     # Geometry utilities
├── gfx.py                     # Graphics classes
├── logging.py                 # Logging utilities
├── metadata.py                # Metadata classes
├── physics.py                 # Physics classes
├── registry.py                # Global registry
├── scene.py                   # Scene classes
├── sensor.py                  # Sensor classes
└── sim.py                     # Simulator backend stubs
```

## API Reference

### Core Classes

#### Simulator
```python
class Simulator:
    """Main simulation class."""
    
    def __init__(self, config: Configuration): ...
    def close(self, destroy: bool = True) -> None: ...
    def seed(self, new_seed: int) -> None: ...
    def reset(self, agent_ids: Optional[Union[int, List[int]]] = None): ...
    def step(self, action: Union[str, int], dt: float = 1/60) -> ObservationDict: ...
    def get_agent(self, agent_id: int = 0) -> Agent: ...
    
    @property
    def pathfinder(self) -> PathFinder: ...
```

#### Configuration
```python
class Configuration:
    """Simulator configuration."""
    
    def __init__(
        self,
        sim_cfg: SimulatorConfiguration,
        agents: List[AgentConfiguration] = None,
        metadata_mediator: Optional[MetadataMediator] = None,
        enable_batch_renderer: bool = False
    ): ...
```

#### Agent
```python
class Agent:
    """Agent entity in simulation."""
    
    def get_state(self) -> AgentState: ...
    def set_state(self, state: AgentState, reset_sensors: bool = True) -> None: ...
    def act(self, action_name: str) -> bool: ...
    
    @property
    def scene_node(self) -> SceneNode: ...
```

### Navigation

#### PathFinder
```python
class PathFinder:
    """Pathfinding on navigation mesh."""
    
    def is_loaded(self) -> bool: ...
    def find_path(self, start: Point, end: Point) -> ShortestPath: ...
```

#### GreedyGeodesicFollower
```python
class GreedyGeodesicFollower:
    """Greedy path follower."""
    
    def next_action_along(self, goal_pos: Point) -> Optional[Action]: ...
    def find_path(self, goal_pos: Point) -> List[Point]: ...
```

### Sensors

All sensor classes follow this pattern:
```python
class SensorSpec:
    uuid: str
    sensor_type: SensorType
    position: List[float]
    orientation: List[float]

class Sensor:
    def get_observation(self) -> Observation: ...
```

Available sensor types:
- `CameraSensor` - Standard camera
- `EquirectangularSensor` - 360° camera
- `FisheyeSensor` - Fisheye camera  
- `AudioSensor` - Audio sensor

### Enums

```python
class SensorType(Enum):
    COLOR = 1
    DEPTH = 2
    SEMANTIC = 4
    # ... more types

class SceneNodeType(Enum):
    EMPTY = 0
    SENSOR = 1
    AGENT = 2
    # ... more types
```

## Testing Your Code

Run the test suite:
```bash
python test_habitat_sim_api.py
```

Run the examples:
```bash
python examples_habitat_sim_api.py
```

## Limitations

- **No execution**: All methods raise `NotImplementedError`
- **No backend**: No rendering, physics, or simulation
- **No dependencies**: Doesn't import numpy at runtime (uses TYPE_CHECKING)
- **Interface only**: Meant for development, not execution

## Transitioning to Real habitat-sim

When you're ready to run your code:

1. Install real habitat-sim:
   ```bash
   conda install habitat-sim -c conda-forge -c aihabitat
   ```

2. Change imports:
   ```python
   # Development (with habitat_sim_api)
   import habitat_sim_api as habitat_sim
   
   # Production (with real habitat_sim)
   import habitat_sim
   ```

3. Your code should work without changes!

## FAQ

**Q: Can I use this for actual simulation?**  
A: No, this is interface-only. Use the real habitat-sim for execution.

**Q: Will my IDE autocomplete work?**  
A: Yes! The package provides full type hints and docstrings.

**Q: Can I use this without numpy?**  
A: Yes! The package has zero dependencies (numpy imports use TYPE_CHECKING).

**Q: How do I keep it updated?**  
A: The package mirrors habitat-sim 0.3.3. For newer versions, regenerate from the source.

**Q: Can I use this in CI/CD?**  
A: Yes! It's perfect for type checking and linting in CI without heavy dependencies.

## Contributing

This package is auto-generated from habitat-sim. To report issues:
- API issues: https://github.com/facebookresearch/habitat-sim/issues
- Package issues: File in the main habitat-sim repository

## License

MIT License - Same as habitat-sim

Copyright (c) Meta Platforms, Inc. and affiliates.
