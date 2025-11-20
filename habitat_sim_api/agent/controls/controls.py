#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Control specifications for habitat_sim_api.
"""

from typing import Any, Dict, Optional

__all__ = [
    "ActuationSpec",
    "SceneNodeControl",
    "ObjectControls",
    "PyRobotNoisyActuationSpec",
]


class ActuationSpec:
    """
    Specification for an actuation (movement) command.
    
    Attributes:
        amount: Magnitude of the actuation
        constraint: Optional constraint on the actuation
    """
    
    def __init__(self, amount: float = 0.0, constraint: Optional[Any] = None):
        self.amount = amount
        self.constraint = constraint


class SceneNodeControl:
    """
    Base class for scene node controls.
    
    Controls define how actions are mapped to scene node transformations.
    """
    
    def __init__(self, body_action: bool = False):
        self.body_action = body_action
    
    def __call__(self, *args, **kwargs):
        """Execute the control action."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ObjectControls:
    """Controls for manipulating objects in the scene."""
    
    def __init__(self):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class PyRobotNoisyActuationSpec(ActuationSpec):
    """
    Actuation specification with PyRobot-style noise.
    
    Extends ActuationSpec with noise parameters for realistic robot behavior.
    """
    
    def __init__(
        self,
        amount: float = 0.0,
        robot_lin_vel_noise: float = 0.0,
        robot_ang_vel_noise: float = 0.0,
        **kwargs
    ):
        super().__init__(amount)
        self.robot_lin_vel_noise = robot_lin_vel_noise
        self.robot_ang_vel_noise = robot_ang_vel_noise
