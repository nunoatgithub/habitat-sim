#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Agent module for habitat_sim_api_v0_2_2.

Defines agents, their configurations, states, and actions.
"""

from typing import Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np

__all__ = ["ActionSpec", "SixDOFPose", "AgentState", "AgentConfiguration", "Agent"]


class ActionSpec:
    """
    Defines how a specific action is implemented.
    
    Attributes:
        name: Name of the function implementing the action in the registry
        actuation: Arguments that will be passed to the function
    """
    
    def __init__(self, name: str, actuation: Optional["ActuationSpec"] = None):
        self.name = name
        self.actuation = actuation


class SixDOFPose:
    """
    Specifies a position with 6 degrees of freedom.
    
    Attributes:
        position: xyz position as numpy array
        rotation: unit quaternion rotation
    """
    
    def __init__(
        self,
        position: Optional[Any] = None,
        rotation: Optional[Union[Any, List]] = None
    ):
        self.position = position if position is not None else [0.0, 0.0, 0.0]
        self.rotation = rotation if rotation is not None else [1.0, 0.0, 0.0, 0.0]


class AgentState:
    """
    State of an agent at a given timestep.
    
    Attributes:
        position: Agent's xyz position
        rotation: Agent's rotation as quaternion
        sensor_states: Dictionary of sensor states keyed by sensor ID
    """
    
    def __init__(
        self,
        position: Optional[Any] = None,
        rotation: Optional[Union[Any, List]] = None,
        sensor_states: Optional[Dict[str, SixDOFPose]] = None
    ):
        self.position = position if position is not None else [0.0, 0.0, 0.0]
        self.rotation = rotation if rotation is not None else [1.0, 0.0, 0.0, 0.0]
        self.sensor_states = sensor_states if sensor_states is not None else {}


class AgentConfiguration:
    """
    Configuration for an agent.
    
    Attributes:
        height: Height of the agent
        radius: Radius of the agent's collision shape
        sensor_specifications: List of sensor specifications
        action_space: Dictionary of available actions
        body_type: Type of collision body (e.g., "cylinder")
    """
    
    def __init__(
        self,
        height: float = 1.5,
        radius: float = 0.1,
        sensor_specifications: Optional[List] = None,
        action_space: Optional[Dict[Any, ActionSpec]] = None,
        body_type: str = "cylinder"
    ):
        self.height = height
        self.radius = radius
        self.sensor_specifications = sensor_specifications or []
        self.action_space = action_space or {}
        self.body_type = body_type


class Agent:
    """
    Agent in the simulation.
    
    An agent is an embodied entity that can take actions and observe the world.
    """
    
    def __init__(self, *args, **kwargs):
        """Initialize agent (stub implementation)."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def get_state(self) -> AgentState:
        """Get the current state of the agent."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def set_state(self, state: AgentState, reset_sensors: bool = True) -> None:
        """Set the state of the agent."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def act(self, action_name: str) -> bool:
        """
        Execute an action.
        
        Args:
            action_name: Name of the action to execute
            
        Returns:
            Whether the action was successful
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    @property
    def scene_node(self):
        """Get the agent's scene node."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
