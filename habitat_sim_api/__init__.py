#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
habitat_sim_api - Interface-only package mirroring habitat-sim Python API

This is a pure-Python, interface-only package that mirrors the Python API
of habitat-sim without any native code or backend implementation.

All classes and methods raise NotImplementedError when called.
This package serves as a contract/interface definition only.
"""

__version__ = "0.3.3-api"

# Import submodules
from habitat_sim_api import (
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
    scene,
    sensor,
    sensors,
    sim,
    simulator,
    utils,
)
from habitat_sim_api.registry import registry

# Import key classes from submodules
from habitat_sim_api.agent.agent import (
    ActionSpec,
    Agent,
    AgentConfiguration,
    AgentState,
    SixDOFPose,
)
from habitat_sim_api.agent.controls.controls import (
    ActuationSpec,
    ObjectControls,
    PyRobotNoisyActuationSpec,
    SceneNodeControl,
)
from habitat_sim_api.agent.controls import (
    controls,
    default_controls,
    object_controls,
    pyrobot_noisy_controls,
)
from habitat_sim_api.bindings import (
    MapStringString,
    ReplayRenderer,
    ReplayRendererConfiguration,
    RigidState,
    SceneGraph,
    SceneNode,
    SceneNodeType,
    SimulatorConfiguration,
    audio_enabled,
    built_with_bullet,
    cuda_enabled,
    stage_id,
)
from habitat_sim_api.nav import (
    GreedyFollowerCodes,
    GreedyGeodesicFollower,
    HitRecord,
    MultiGoalShortestPath,
    NavMeshSettings,
    PathFinder,
    ShortestPath,
    VectorGreedyCodes,
)
from habitat_sim_api.sensor import (
    AudioSensor,
    AudioSensorSpec,
    CameraSensorSpec,
    EquirectangularSensor,
    EquirectangularSensorSpec,
    FisheyeSensorDoubleSphereSpec,
    FisheyeSensorModelType,
    FisheyeSensorSpec,
    RLRAudioPropagationChannelLayout,
    RLRAudioPropagationChannelLayoutType,
    RLRAudioPropagationConfiguration,
    Sensor,
    SensorFactory,
    SensorSpec,
    SensorSubType,
    SensorType,
    VisualSensorSpec,
)
from habitat_sim_api.simulator import Configuration, Simulator

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
    "ReplayRenderer",
    "ReplayRendererConfiguration",
    "RigidState",
    "SceneGraph",
    "SceneNode",
    "SceneNodeType",
    "SimulatorConfiguration",
    "audio_enabled",
    "built_with_bullet",
    "cuda_enabled",
    "stage_id",
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
    "RLRAudioPropagationChannelLayoutType",
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
