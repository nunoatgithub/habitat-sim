# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Geometry module for habitat_sim_api.

Encapsulates global geometry utilities.
"""

from typing import List, Tuple, Any, TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


class OBB:
    """Oriented Bounding Box."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class Ray:
    """Ray for raycasting."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


# Common direction vectors
UP: Tuple[float, float, float] = (0.0, 1.0, 0.0)
GRAVITY: Tuple[float, float, float] = (0.0, -9.8, 0.0)
FRONT: Tuple[float, float, float] = (0.0, 0.0, -1.0)
BACK: Tuple[float, float, float] = (0.0, 0.0, 1.0)
LEFT: Tuple[float, float, float] = (-1.0, 0.0, 0.0)
RIGHT: Tuple[float, float, float] = (1.0, 0.0, 0.0)


def build_catmull_rom_spline(
    points: List[Any], num_samples: int = 100
) -> List[Any]:
    """
    Build a Catmull-Rom spline through the given points.
    
    Args:
        points: Control points for the spline
        num_samples: Number of samples along the spline
        
    Returns:
        List of points along the spline
    """
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def compute_gravity_aligned_MOBB(points: List[Any]) -> OBB:
    """
    Compute minimum oriented bounding box aligned with gravity.
    
    Args:
        points: Points to bound
        
    Returns:
        The oriented bounding box
    """
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def get_transformed_bb(obb: OBB, transform: Any) -> OBB:
    """
    Get a transformed oriented bounding box.
    
    Args:
        obb: Original bounding box
        transform: Transformation matrix
        
    Returns:
        Transformed bounding box
    """
    raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = [
    "OBB",
    "UP",
    "GRAVITY",
    "FRONT",
    "BACK",
    "LEFT",
    "RIGHT",
    "build_catmull_rom_spline",
    "compute_gravity_aligned_MOBB",
    "get_transformed_bb",
    "Ray",
]
