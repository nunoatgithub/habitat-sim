# habitat-sim-api-v0-2-2

**Pure-Python, interface-only package mirroring the habitat-sim Python API**

This package provides a complete interface definition for [habitat-sim](https://github.com/facebookresearch/habitat-sim) without any native code, compiled extensions, or runtime behavior. It serves as a contract layer for:

- Type checking and static analysis
- API documentation and reference
- Version-agnostic interface definitions
- Lightweight development environments

## Features

- ✅ **Pure Python** - No C++ compilation required
- ✅ **Zero Dependencies** - No external packages needed (not even numpy)
- ✅ **Python 3.8+** - Compatible with modern Python versions
- ✅ **Complete API** - Mirrors all public classes, methods, and functions from habitat-sim
- ✅ **Type Hints** - Full typing support for IDEs and type checkers
- ✅ **Interface Only** - All methods raise `NotImplementedError`

## Installation

### From source

```bash
cd habitat_sim_api_v0_2_2
pip install -e .
```

Or using the standalone setup:

```bash
python habitat_sim_api_v0_2_2_setup.py install
```

## Usage

Import and use the package exactly as you would with habitat-sim:

```python
import habitat_sim_api_v0_2_2 as habitat_sim

# All classes are available
from habitat_sim_api_v0_2_2 import Simulator, Agent, Configuration

# Type checking works
config = habitat_sim.Configuration(
    sim_cfg=habitat_sim.SimulatorConfiguration(),
    agents=[]
)

# But execution raises NotImplementedError
try:
    sim = habitat_sim.Simulator(config)
except NotImplementedError:
    print("This is an interface-only package!")
```

## Package Structure

The package mirrors the exact structure of habitat-sim:

```
habitat_sim_api_v0_2_2/
├── __init__.py                 # Main package with top-level imports
├── agent/                      # Agent definitions
│   ├── agent.py               # Agent, AgentState, AgentConfiguration
│   └── controls/              # Control specifications
├── bindings.py                # C++ binding stubs (SceneNode, Sensor, etc.)
├── simulator.py               # Simulator and Configuration classes
├── nav/                       # Navigation and pathfinding
├── sensors/                   # Sensor specifications and noise models
├── utils/                     # Utility functions
├── physics.py                 # Physics-related classes
├── attributes.py              # Attribute definitions
├── scene.py                   # Scene and semantic classes
└── ...                        # Other modules
```

## What's Included

All major habitat-sim components:

### Core
- `Simulator` - Main simulation class
- `Configuration` - Simulator configuration
- `SimulatorConfiguration` - Backend configuration

### Agents
- `Agent` - Agent entity
- `AgentConfiguration` - Agent configuration
- `AgentState` - Agent state representation
- `ActionSpec` - Action specifications
- `SixDOFPose` - 6DOF pose representation

### Navigation
- `PathFinder` - Pathfinding on navmesh
- `GreedyGeodesicFollower` - Greedy path following
- `NavMeshSettings` - Navmesh configuration
- `ShortestPath` - Shortest path representation

### Sensors
- `Sensor`, `SensorSpec` - Base sensor classes
- `CameraSensor`, `CameraSensorSpec` - Camera sensors
- `EquirectangularSensor` - 360° sensors
- `FisheyeSensor` - Fisheye sensors
- `AudioSensor` - Audio sensors
- Noise models: `GaussianNoiseModel`, `RedwoodDepthNoiseModel`, etc.

### Physics
- `ManagedRigidObject` - Rigid body objects
- `ManagedArticulatedObject` - Articulated objects
- Motion types and collision helpers

### Utilities
- Quaternion utilities
- Visualization helpers
- Settings and validators
- Manager utilities

### Scene & Semantics
- `SemanticScene` - Semantic scene representation
- `SemanticCategory`, `SemanticObject`, `SemanticRegion`

## Use Cases

### 1. Type Checking

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import habitat_sim_api_v0_2_2 as habitat_sim

def setup_agent(config: "habitat_sim.AgentConfiguration") -> None:
    # IDE autocomplete and type checking work!
    print(f"Agent height: {config.height}")
```

### 2. Documentation Generation

Use this package to generate API documentation without needing to build the full habitat-sim with all its C++ dependencies.

### 3. Development Without Native Dependencies

Develop code that uses habitat-sim's API without needing to compile the C++ backend. Switch to the real habitat-sim for execution.

### 4. API Reference

Explore the habitat-sim API structure and available classes/methods:

```python
import habitat_sim_api_v0_2_2
import inspect

# List all available classes
for name in dir(habitat_sim_api_v0_2_2):
    obj = getattr(habitat_sim_api_v0_2_2, name)
    if inspect.isclass(obj):
        print(f"{name}: {obj.__doc__}")
```

## Limitations

⚠️ **This is an interface-only package**

- All method bodies raise `NotImplementedError`
- No simulation, rendering, or physics execution
- No dependency on native libraries (Bullet, Magnum, etc.)
- For execution, use the real [habitat-sim](https://github.com/facebookresearch/habitat-sim) package

## Relationship to habitat-sim

This package is **not a replacement** for habitat-sim. It is:
- A lightweight interface definition
- For static analysis and type checking
- For environments where compiling habitat-sim is not feasible

For actual simulation, install the real habitat-sim:
```bash
conda install habitat-sim -c conda-forge -c aihabitat
```

## Version Compatibility

This package mirrors habitat-sim version **0.2.2**. The API surface should remain compatible across minor versions, but check the habitat-sim changelog for breaking changes.

## Contributing

This is an auto-generated interface package. To report issues or suggest improvements:

1. For habitat-sim API issues: https://github.com/facebookresearch/habitat-sim/issues
2. For this package specifically: File an issue in the main habitat-sim repository

## License

MIT License - Same as habitat-sim

Copyright (c) Meta Platforms, Inc. and affiliates.

## See Also

- [habitat-sim](https://github.com/facebookresearch/habitat-sim) - The full simulator
- [habitat-lab](https://github.com/facebookresearch/habitat-lab) - High-level embodied AI library
- [AI Habitat](https://aihabitat.org/) - Project homepage
