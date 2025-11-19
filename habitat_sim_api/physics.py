# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Physics module for habitat_sim_api."""

from typing import Any


class MotionType:
    """Motion type enum for physics objects."""
    STATIC = 0
    KINEMATIC = 1
    DYNAMIC = 2


class CollisionGroupHelper:
    """Helper for managing collision groups."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ContactPointData:
    """Data about a contact point in physics simulation."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class JointMotorSettings:
    """Settings for joint motors."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ManagedArticulatedObject:
    """Managed articulated object for physics simulation."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ManagedBulletArticulatedObject:
    """Bullet-based articulated object."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ManagedBulletRigidObject:
    """Bullet-based rigid object."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ManagedRigidObject:
    """Managed rigid object for physics simulation."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class PhysicsSimulationLibrary:
    """Physics simulation library enum."""
    NONE = 0
    BULLET = 1


class RayHitInfo:
    """Information about a ray hit in physics."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class RaycastResults:
    """Results from a raycast query."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class VelocityControl:
    """Velocity control for physics objects."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = [
    "MotionType",
    "CollisionGroupHelper",
    "ContactPointData",
    "JointMotorSettings",
    "ManagedArticulatedObject",
    "ManagedBulletArticulatedObject",
    "ManagedBulletRigidObject",
    "ManagedRigidObject",
    "PhysicsSimulationLibrary",
    "RayHitInfo",
    "RaycastResults",
    "VelocityControl",
]
