#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Mobile manipulator robot stubs."""

from typing import Any, Dict, List, Optional


class RobotCameraParams:
    """Parameters for robot cameras."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class MobileManipulatorParams:
    """Parameters for mobile manipulator robots."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class MobileManipulator:
    """Mobile manipulator robot."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def reconfigure(self) -> None:
        """Reconfigure the robot."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def update(self) -> None:
        """Update robot state."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def reset(self) -> None:
        """Reset the robot."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    @property
    def base_pos(self) -> Any:
        """Get base position."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    @property
    def base_rot(self) -> Any:
        """Get base rotation."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = ["RobotCameraParams", "MobileManipulatorParams", "MobileManipulator"]
