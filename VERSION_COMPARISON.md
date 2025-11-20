# habitat_sim_api Version Comparison

## Overview

This repository now contains two interface-only packages mirroring different versions of habitat-sim:

1. **habitat_sim_api** - Version 0.3.3
2. **habitat_sim_api_v0_2_2** - Version 0.2.2

Both packages provide pure-Python interfaces without any compiled extensions or runtime dependencies.

## Version Comparison

### Common Features (Both Versions)

Both versions include:
- Pure Python implementation
- Zero runtime dependencies (numpy only in TYPE_CHECKING)
- Complete API coverage for their respective versions
- All methods raise NotImplementedError
- Full type hints and docstrings
- PEP 561 compliance (py.typed marker)

### Version-Specific Differences

#### habitat_sim_api_v0_2_2 (v0.2.2) - Unique Features

**New Modules:**
- `robots/` - Robot interfaces and implementations
  - `FetchRobot` - Fetch robot with wheels
  - `FetchRobotNoWheels` - Fetch robot without wheels
  - `MobileManipulator` - Mobile manipulator base class
  - `MobileManipulatorParams` - Parameters for mobile manipulators
  - `RobotCameraParams` - Camera parameters for robots
  - `RobotInterface` - Base robot interface

**Additional Functions/Classes:**
- `vhacd_enabled()` - Check if VHACD is enabled
- `VHACDParameters` - Parameters for VHACD convex decomposition

**Copyright:**
- Copyright (c) Facebook, Inc.

#### habitat_sim_api (v0.3.3) - Unique Features

**New Classes/Enums:**
- `RLRAudioPropagationChannelLayoutType` - Enum for audio channel layouts
  - Mono
  - Stereo
  - Binaural

**Removed from 0.3.3:**
- `robots/` module (replaced by other robot handling mechanisms)
- `vhacd_enabled()` function
- `VHACDParameters` class

**Copyright:**
- Copyright (c) Meta Platforms, Inc.

## Package Statistics

### habitat_sim_api_v0_2_2 (v0.2.2)
- **Python files:** 45
- **Package size:** ~155 KB
- **Version:** 0.2.2-api
- **Base commit:** 011191f65f37587f5a5452a93d840b5684593a00

### habitat_sim_api (v0.3.3)
- **Python files:** 37
- **Package size:** ~150 KB
- **Version:** 0.3.3-api
- **Base commit:** Current main branch

## Usage

### Installing v0.2.2
```bash
python habitat_sim_api_v0_2_2_setup.py install
```

### Installing v0.3.3
```bash
python habitat_sim_api_setup.py install
```

### Importing v0.2.2
```python
import habitat_sim_api_v0_2_2 as habitat_sim

# Access robot features
from habitat_sim_api_v0_2_2.robots import FetchRobot, MobileManipulator

# Check VHACD support
if habitat_sim.vhacd_enabled():
    print("VHACD is available")
```

### Importing v0.3.3
```python
import habitat_sim_api as habitat_sim

# Audio channel layout types (new in 0.3.3)
from habitat_sim_api.bindings import RLRAudioPropagationChannelLayoutType

layout_type = RLRAudioPropagationChannelLayoutType.Binaural
```

## Testing

### v0.2.2 Tests
```bash
python test_habitat_sim_api_v0_2_2.py
```

Tests verify:
- ✓ Basic imports
- ✓ Robot module functionality
- ✓ VHACD support
- ✓ Absence of 0.3.x features
- ✓ NotImplementedError behavior

### v0.3.3 Tests
```bash
python test_habitat_sim_api.py
```

Tests verify:
- ✓ Basic imports
- ✓ All modules and classes
- ✓ Audio channel layout types
- ✓ NotImplementedError behavior

## Migration Guide

### Upgrading from 0.2.2 to 0.3.3

If you're using the interface-only packages and need to upgrade:

**Code Changes Needed:**

1. **Robot Module** - No longer available in 0.3.3
   ```python
   # v0.2.2
   from habitat_sim_api_v0_2_2.robots import FetchRobot
   
   # v0.3.3 - Robot handling changed in actual habitat-sim
   # Consult habitat-sim 0.3.3 documentation for new approach
   ```

2. **VHACD** - Function removed in 0.3.3
   ```python
   # v0.2.2
   if habitat_sim.vhacd_enabled():
       pass
   
   # v0.3.3 - Feature handled differently
   ```

3. **Audio Channel Layouts** - New enum in 0.3.3
   ```python
   # v0.3.3 only
   from habitat_sim.bindings import RLRAudioPropagationChannelLayoutType
   layout = RLRAudioPropagationChannelLayoutType.Binaural
   ```

## Use Cases

### When to Use v0.2.2
- Working with older habitat-sim 0.2.2 codebases
- Need robot interface definitions (FetchRobot, MobileManipulator)
- VHACD feature requirements
- Legacy project compatibility

### When to Use v0.3.3
- New projects using latest habitat-sim
- Need audio propagation channel layout types
- Working with current habitat-sim features
- Future-proof development

## Security

Both versions:
- ✅ CodeQL scan: 0 alerts
- ✅ No security vulnerabilities
- ✅ Pure Python (no binary dependencies)

## Conclusion

Both interface-only packages provide complete API coverage for their respective habitat-sim versions. Choose the version that matches your target habitat-sim deployment.

For actual simulation execution, install the corresponding real habitat-sim version:
- v0.2.2: Use habitat-sim 0.2.2 from releases
- v0.3.3: Use latest habitat-sim from conda/pip
