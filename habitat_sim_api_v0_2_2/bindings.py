# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Stub implementations for habitat_sim bindings.

In the real habitat_sim, these are C++ classes exposed via pybind11.
Here they are pure Python stubs for interface compatibility.
"""

from typing import Any, Dict, List, Optional
from enum import Enum


class MapStringString(Dict[str, str]):
    """A dictionary mapping strings to strings."""
    pass


class SceneNodeType(Enum):
    """Scene node types."""
    EMPTY = 0
    SENSOR = 1
    AGENT = 2
    CAMERA = 3
    OBJECT = 4


class SceneNode:
    """Stub for SceneNode - represents a node in the scene graph."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class SceneGraph:
    """Stub for SceneGraph - manages the scene node hierarchy."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class RigidState:
    """Stub for RigidState - represents the state of a rigid body."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class Configuration:
    """Stub for Configuration - general configuration class."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ConfigValType(Enum):
    """Configuration value types."""
    Unknown = 0
    Boolean = 1
    Integer = 2
    Double = 3
    String = 4
    MagnumVec3 = 5
    MagnumQuat = 6
    MagnumMat3 = 7
    MagnumRad = 8


class SimulatorConfiguration:
    """Stub for SimulatorConfiguration - configuration for the simulator backend."""
    
    def __init__(self):
        self.scene_id: str = ""
        self.scene_dataset_config_file: str = ""
        self.enable_physics: bool = False
        self.physics_config_file: str = ""
        self.override_scene_light_defaults: bool = False
        self.scene_light_setup: str = ""
        self.load_semantic_mesh: bool = False
        self.force_separate_semantic_scene_graph: bool = False
        self.create_renderer: bool = True
        self.leave_context_with_background_renderer: bool = False
        self.enable_gfx_replay_save: bool = False
        self.frustum_culling: bool = False
        self.requires_textures: bool = True
        self.random_seed: int = 0


class ReplayRendererConfiguration:
    """Stub for ReplayRendererConfiguration."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ReplayRenderer:
    """Stub for ReplayRenderer - for replaying recorded simulations."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


# Sensor-related classes
class SensorType(Enum):
    """Types of sensors."""
    NONE = 0
    COLOR = 1
    DEPTH = 2
    NORMAL = 3
    SEMANTIC = 4
    PATH = 5
    GOAL = 6
    FORCE = 7
    TENSOR = 8
    TEXT = 9
    AUDIO = 10


class SensorSubType(Enum):
    """Sensor subtypes."""
    NONE = 0
    PINHOLE = 1
    ORTHOGRAPHIC = 2
    FISHEYE = 3
    EQUIRECTANGULAR = 4


class SensorSpec:
    """Stub for SensorSpec - specification for a sensor."""
    
    def __init__(self):
        self.uuid: str = ""
        self.sensor_type: SensorType = SensorType.NONE
        self.sensor_subtype: SensorSubType = SensorSubType.NONE
        self.position: List[float] = [0.0, 0.0, 0.0]
        self.orientation: List[float] = [0.0, 0.0, 0.0]


class VisualSensorSpec(SensorSpec):
    """Stub for VisualSensorSpec - specification for visual sensors."""
    
    def __init__(self):
        super().__init__()
        self.resolution: List[int] = [128, 128]
        self.channels: int = 3
        self.gpu2gpu_transfer: bool = False


class CameraSensorSpec(VisualSensorSpec):
    """Stub for CameraSensorSpec - specification for camera sensors."""
    
    def __init__(self):
        super().__init__()
        self.far: float = 1000.0
        self.near: float = 0.01
        self.hfov: float = 90.0
        self.ortho_scale: float = 0.1


class CubeMapSensorBaseSpec(VisualSensorSpec):
    """Stub for CubeMapSensorBaseSpec."""
    
    def __init__(self):
        super().__init__()


class EquirectangularSensorSpec(CubeMapSensorBaseSpec):
    """Stub for EquirectangularSensorSpec."""
    
    def __init__(self):
        super().__init__()


class FisheyeSensorModelType(Enum):
    """Fisheye sensor model types."""
    DOUBLE_SPHERE = 0


class FisheyeSensorSpec(VisualSensorSpec):
    """Stub for FisheyeSensorSpec."""
    
    def __init__(self):
        super().__init__()
        self.focal_length: List[float] = [1.0, 1.0]
        self.principal_point_offset: Optional[List[float]] = None


class FisheyeSensorDoubleSphereSpec(FisheyeSensorSpec):
    """Stub for FisheyeSensorDoubleSphereSpec."""
    
    def __init__(self):
        super().__init__()
        self.alpha: float = 0.59
        self.xi: float = -0.18


class AudioSensorSpec(SensorSpec):
    """Stub for AudioSensorSpec."""
    
    def __init__(self):
        super().__init__()


class RLRAudioPropagationChannelLayout:
    """Stub for RLRAudioPropagationChannelLayout."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class RLRAudioPropagationConfiguration:
    """Stub for RLRAudioPropagationConfiguration."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class Sensor:
    """Stub for Sensor - base sensor class."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class VisualSensor(Sensor):
    """Stub for VisualSensor."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class CameraSensor(VisualSensor):
    """Stub for CameraSensor."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class CubeMapSensorBase(VisualSensor):
    """Stub for CubeMapSensorBase."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class EquirectangularSensor(CubeMapSensorBase):
    """Stub for EquirectangularSensor."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class FisheyeSensor(VisualSensor):
    """Stub for FisheyeSensor."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class AudioSensor(Sensor):
    """Stub for AudioSensor."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class SensorFactory:
    """Stub for SensorFactory - factory for creating sensors."""
    
    @staticmethod
    def create_sensors(*args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class Observation:
    """Stub for Observation."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


# Navigation classes
class ShortestPath:
    """Stub for ShortestPath."""
    
    def __init__(self):
        self.requested_start: List[float] = []
        self.requested_end: List[float] = []
        self.points: List[List[float]] = []
        self.geodesic_distance: float = float('inf')


class MultiGoalShortestPath:
    """Stub for MultiGoalShortestPath."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class PathFinder:
    """Stub for PathFinder - handles pathfinding on navmesh."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def is_loaded(self) -> bool:
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def find_path(self, *args, **kwargs) -> ShortestPath:
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class NavMeshSettings:
    """Stub for NavMeshSettings - settings for navigation mesh."""
    
    def __init__(self):
        self.cell_size: float = 0.05
        self.cell_height: float = 0.2
        self.agent_height: float = 1.5
        self.agent_radius: float = 0.1
        self.agent_max_climb: float = 0.2
        self.agent_max_slope: float = 45.0


class GreedyFollowerCodes(Enum):
    """Status codes for greedy geodesic follower."""
    ERROR = 0
    FORWARD = 1
    LEFT = 2
    RIGHT = 3
    STOP = 4


class VectorGreedyCodes:
    """Stub for VectorGreedyCodes - vector of greedy codes."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class GreedyGeodesicFollowerImpl:
    """Stub for GreedyGeodesicFollowerImpl."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class HitRecord:
    """Stub for HitRecord - represents a ray hit."""
    
    def __init__(self, *args, **kwargs):
        self.hit_pos: List[float] = []
        self.hit_normal: List[float] = []
        self.hit_dist: float = 0.0


# Simulator backend
class Simulator:
    """Stub for Simulator backend (the C++ implementation)."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


# Utility functions
def audio_enabled() -> bool:
    """Check if audio is enabled."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def built_with_bullet() -> bool:
    """Check if built with Bullet physics."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def cuda_enabled() -> bool:
    """Check if CUDA is enabled."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def stage_id(*args, **kwargs):
    """Get stage ID."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def vhacd_enabled() -> bool:
    """Check if VHACD (Volumetric Hierarchical Approximate Convex Decomposition) is enabled."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


class VHACDParameters:
    """Parameters for VHACD convex decomposition."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = [
    "AudioSensor",
    "AudioSensorSpec",
    "CameraSensor",
    "CameraSensorSpec",
    "Configuration",
    "ConfigValType",
    "CubeMapSensorBase",
    "CubeMapSensorBaseSpec",
    "EquirectangularSensor",
    "EquirectangularSensorSpec",
    "FisheyeSensor",
    "FisheyeSensorDoubleSphereSpec",
    "FisheyeSensorModelType",
    "FisheyeSensorSpec",
    "GreedyFollowerCodes",
    "GreedyGeodesicFollowerImpl",
    "HitRecord",
    "MapStringString",
    "MultiGoalShortestPath",
    "NavMeshSettings",
    "Observation",
    "PathFinder",
    "ReplayRenderer",
    "ReplayRendererConfiguration",
    "RigidState",
    "RLRAudioPropagationChannelLayout",
    "RLRAudioPropagationConfiguration",
    "SceneGraph",
    "SceneNode",
    "SceneNodeType",
    "Sensor",
    "SensorFactory",
    "SensorSpec",
    "SensorSubType",
    "SensorType",
    "ShortestPath",
    "Simulator",
    "SimulatorConfiguration",
    "VectorGreedyCodes",
    "VisualSensor",
    "VisualSensorSpec",
    "audio_enabled",
    "built_with_bullet",
    "cuda_enabled",
    "stage_id",
    "vhacd_enabled",
    "VHACDParameters",
]
