#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Common utility functions for habitat_sim_api."""

from typing import Any, List, TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


def quat_from_coeffs(coeffs: List[float]) -> Any:
    """Create quaternion from coefficients."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def quat_from_magnum(quat: Any) -> Any:
    """Convert Magnum quaternion to numpy quaternion."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def quat_to_magnum(quat: Any) -> Any:
    """Convert numpy quaternion to Magnum quaternion."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def quat_from_angle_axis(angle: float, axis: Any) -> Any:
    """Create quaternion from angle and axis."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def quat_rotate_vector(quat: Any, vector: Any) -> Any:
    """Rotate a vector by a quaternion."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def quat_from_two_vectors(v1: Any, v2: Any) -> Any:
    """Create quaternion representing rotation from v1 to v2."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def angle_between_quats(q1: Any, q2: Any) -> float:
    """Compute angle between two quaternions."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = [
    "quat_from_coeffs",
    "quat_from_magnum",
    "quat_to_magnum",
    "quat_from_angle_axis",
    "quat_rotate_vector",
    "quat_from_two_vectors",
    "angle_between_quats",
]
