# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Sensor suite for managing multiple sensors."""

from typing import Dict, Any


class SensorSuite:
    """Container for a suite of sensors attached to an agent."""
    
    def __init__(self, sensors: Dict[str, Any]):
        """
        Initialize the sensor suite.
        
        Args:
            sensors: Dictionary mapping sensor IDs to sensor instances
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def get(self, sensor_id: str) -> Any:
        """Get a sensor by ID."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = ["SensorSuite"]
