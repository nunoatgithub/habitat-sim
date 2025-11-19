# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Greedy geodesic follower for navigation."""

from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


class GreedyGeodesicFollower:
    """
    Planner that greedily fits actions to follow the geodesic shortest path.
    
    The planner plans on perfect actions (assumes actuation noise is unbiased).
    """
    
    def __init__(
        self,
        pathfinder: "PathFinder",
        agent: "Agent",
        goal_radius: Optional[float] = None,
        *,
        stop_key: Optional[Any] = None,
        forward_key: Optional[Any] = None,
        left_key: Optional[Any] = None,
        right_key: Optional[Any] = None,
        fix_thrashing: bool = True,
        thrashing_threshold: int = 16,
    ) -> None:
        """
        Initialize the greedy geodesic follower.
        
        Args:
            pathfinder: Instance of the pathfinder with loaded navmesh
            agent: Agent to fit actions for
            goal_radius: How close the agent must get to the goal
            stop_key: Action key to emit when agent should stop
            forward_key: Action key for move_forward
            left_key: Action key for turn_left
            right_key: Action key for turn_right
            fix_thrashing: Whether to attempt to fix thrashing
            thrashing_threshold: Number of actions in a left/right cycle
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def next_action_along(self, goal_pos: Any) -> Optional[Any]:
        """
        Get the next action to take along the path to the goal.
        
        Args:
            goal_pos: The goal position
            
        Returns:
            The next action to take, or None if goal is reached
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    def find_path(self, goal_pos: Any) -> List[Any]:
        """
        Find a path to the goal position.
        
        Args:
            goal_pos: The goal position
            
        Returns:
            List of positions along the path
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = ["GreedyGeodesicFollower"]
