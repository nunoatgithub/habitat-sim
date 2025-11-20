#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Fetch robot stubs."""

from typing import Any


class FetchRobot:
    """Fetch robot with wheels."""
    
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


class FetchRobotNoWheels:
    """Fetch robot without wheels."""
    
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


__all__ = ["FetchRobot", "FetchRobotNoWheels"]
