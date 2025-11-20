#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
habitat_sim_api_v0_2_2 - Interface-only package mirroring habitat-sim Python API v0.2.2

This is a pure-Python, interface-only package that mirrors the Python API
of habitat-sim version 0.2.2 without any native code or backend implementation.

All classes and methods raise NotImplementedError when called.
This package serves as a contract/interface definition only.
"""

__version__ = "0.2.2-api"

# Import submodules
from habitat_sim_api_v0_2_2 import (
    agent,
    attributes,
    attributes_managers,
    errors,
    geo,
    gfx,
    logging,
    metadata,
    nav,
    physics,
    robots,
    scene,
    sensor,
    sensors,
    sim,
    simulator,
    utils,
)
from habitat_sim_api_v0_2_2.registry import registry

# Import key classes from submodules
from habitat_sim_api_v0_2_2.agent.agent import (
    ActionSpec,
    Agent,
    AgentConfiguration,
    AgentState,
    SixDOFPose,
)
from habitat_sim_api_v0_2_2.agent.controls.controls import (
    ActuationSpec,
    ObjectControls,
    PyRobotNoisyActuationSpec,
    SceneNodeControl,
)
from habitat_sim_api_v0_2_2.agent.controls import (
    controls,
    default_controls,
    object_controls,
    pyrobot_noisy_controls,
)
from habitat_sim_api_v0_2_2.bindings import (
    MapStringString,
    RigidState,
    SceneGraph,
    SceneNode,
    SceneNodeType,
    SimulatorConfiguration,
    audio_enabled,
    built_with_bullet,
    cuda_enabled,
    vhacd_enabled,
)
from habitat_sim_api_v0_2_2.nav import (
    GreedyFollowerCodes,
    GreedyGeodesicFollower,
    HitRecord,
    MultiGoalShortestPath,
    NavMeshSettings,
    PathFinder,
    ShortestPath,
    VectorGreedyCodes,
)
from habitat_sim_api_v0_2_2.sensor import (
    AudioSensor,
    AudioSensorSpec,
    CameraSensorSpec,
    EquirectangularSensor,
    EquirectangularSensorSpec,
    FisheyeSensorDoubleSphereSpec,
    FisheyeSensorModelType,
    FisheyeSensorSpec,
    RLRAudioPropagationChannelLayout,
    RLRAudioPropagationConfiguration,
    Sensor,
    SensorFactory,
    SensorSpec,
    SensorSubType,
    SensorType,
    VisualSensorSpec,
)
from habitat_sim_api_v0_2_2.simulator import Configuration, Simulator

__all__ = [
    "agent",
    "attributes",
    "attributes_managers",
    "metadata",
    "nav",
    "sensors",
    "errors",
    "geo",
    "gfx",
    "logging",
    "physics",
    "robots",
    "scene",
    "sensor",
    "sim",
    "simulator",
    "utils",
    "MapStringString",
    "registry",
    # Agent related
    "ActionSpec",
    "Agent",
    "AgentConfiguration",
    "AgentState",
    "SixDOFPose",
    "ActuationSpec",
    "ObjectControls",
    "PyRobotNoisyActuationSpec",
    "SceneNodeControl",
    # Bindings
    "RigidState",
    "SceneGraph",
    "SceneNode",
    "SceneNodeType",
    "SimulatorConfiguration",
    "audio_enabled",
    "built_with_bullet",
    "cuda_enabled",
    "vhacd_enabled",
    # Nav
    "GreedyFollowerCodes",
    "GreedyGeodesicFollower",
    "HitRecord",
    "MultiGoalShortestPath",
    "NavMeshSettings",
    "PathFinder",
    "ShortestPath",
    "VectorGreedyCodes",
    # Sensors
    "AudioSensor",
    "AudioSensorSpec",
    "CameraSensorSpec",
    "EquirectangularSensor",
    "EquirectangularSensorSpec",
    "FisheyeSensorDoubleSphereSpec",
    "FisheyeSensorModelType",
    "FisheyeSensorSpec",
    "RLRAudioPropagationChannelLayout",
    "RLRAudioPropagationConfiguration",
    "Sensor",
    "SensorFactory",
    "SensorSpec",
    "SensorSubType",
    "SensorType",
    "VisualSensorSpec",
    # Simulator
    "Configuration",
    "Simulator",
]
