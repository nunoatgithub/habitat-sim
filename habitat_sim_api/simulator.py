#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Simulator module for habitat_sim_api.

The simulator ties together the backend, agents, controls, navigation,
and physics simulation.
"""

from typing import Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


# Type aliases
ObservationDict = Dict[str, Union[bool, Any]]


class Configuration:
    """
    Configuration for the simulator.
    
    Ties together a backend config and agent configurations.
    
    Attributes:
        sim_cfg: Configuration for the simulator backend
        agents: List of agent configurations
        metadata_mediator: Optional metadata mediator
        enable_batch_renderer: Whether to enable batch rendering
    """
    
    def __init__(
        self,
        sim_cfg: "SimulatorConfiguration",
        agents: Optional[List["AgentConfiguration"]] = None,
        metadata_mediator: Optional[Any] = None,
        enable_batch_renderer: bool = False
    ):
        from habitat_sim_api.bindings import SimulatorConfiguration
        from habitat_sim_api.agent import AgentConfiguration
        
        self.sim_cfg = sim_cfg
        self.agents = agents or []
        self.metadata_mediator = metadata_mediator
        self.enable_batch_renderer = enable_batch_renderer


class Simulator:
    """
    The core class of habitat-sim.
    
    The simulator ties together the backend, the agent, controls functions,
    NavMesh collision checking/pathfinding, attribute template management,
    object manipulation, and physics simulation.
    """
    
    def __init__(self, config: Configuration):
        """
        Initialize the simulator.
        
        Args:
            config: Configuration for the simulator
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def close(self, destroy: bool = True) -> None:
        """
        Close the simulator instance.
        
        Args:
            destroy: Whether to force the OpenGL context to be destroyed
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def seed(self, new_seed: int) -> None:
        """
        Set the random seed for the simulator.
        
        Args:
            new_seed: The new random seed
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def reset(
        self, agent_ids: Union[Optional[int], List[int]] = None
    ) -> Union[ObservationDict, Dict[int, ObservationDict]]:
        """
        Reset the simulation state.
        
        Args:
            agent_ids: Optional agent IDs for which to return observations
            
        Returns:
            Sensor observations in the reset state
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def step(
        self, action: Union[str, int], dt: float = 1.0 / 60.0
    ) -> ObservationDict:
        """
        Step the simulation forward by one timestep.
        
        Args:
            action: The action to take
            dt: Time step duration
            
        Returns:
            Sensor observations after the step
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def get_sensor_observations(
        self, agent_ids: Optional[List[int]] = None
    ) -> Dict[int, ObservationDict]:
        """
        Get sensor observations for the specified agents.
        
        Args:
            agent_ids: Optional list of agent IDs
            
        Returns:
            Dictionary mapping agent IDs to their observations
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def get_agent(self, agent_id: int = 0) -> "Agent":
        """
        Get an agent by ID.
        
        Args:
            agent_id: The agent ID
            
        Returns:
            The agent
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def initialize_agent(
        self, agent_id: int = 0, initial_state: Optional["AgentState"] = None
    ) -> "Agent":
        """
        Initialize an agent.
        
        Args:
            agent_id: The agent ID
            initial_state: Optional initial state for the agent
            
        Returns:
            The initialized agent
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def reset_agent(self, agent_id: int = 0) -> "AgentState":
        """
        Reset an agent to its initial state.
        
        Args:
            agent_id: The agent ID
            
        Returns:
            The agent's new state
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    @property
    def pathfinder(self) -> "PathFinder":
        """Get the pathfinder for navigation."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    @property
    def renderer(self) -> Any:
        """Get the renderer."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    @property
    def agents(self) -> List["Agent"]:
        """Get the list of agents."""
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def __enter__(self) -> "Simulator":
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close(destroy=True)


__all__ = ["Configuration", "Simulator", "ObservationDict"]
