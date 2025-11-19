# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Attributes module for habitat_sim_api.

Attributes objects store metadata relevant to specific types of simulation objects.
"""

from typing import Any


class ArticulatedObjectAttributes:
    """Attributes for articulated objects."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class CapsulePrimitiveAttributes:
    """Attributes for capsule primitives."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ConePrimitiveAttributes:
    """Attributes for cone primitives."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class CubePrimitiveAttributes:
    """Attributes for cube primitives."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class CylinderPrimitiveAttributes:
    """Attributes for cylinder primitives."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class IcospherePrimitiveAttributes:
    """Attributes for icosphere primitives."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class MarkerSets:
    """Marker sets for objects."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ObjectAttributes:
    """Attributes for generic objects."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class PbrShaderAttributes:
    """Attributes for PBR shaders."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class PhysicsManagerAttributes:
    """Attributes for physics managers."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class StageAttributes:
    """Attributes for stages/scenes."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class UVSpherePrimitiveAttributes:
    """Attributes for UV sphere primitives."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = [
    "ArticulatedObjectAttributes",
    "CapsulePrimitiveAttributes",
    "ConePrimitiveAttributes",
    "CubePrimitiveAttributes",
    "CylinderPrimitiveAttributes",
    "IcospherePrimitiveAttributes",
    "MarkerSets",
    "ObjectAttributes",
    "PbrShaderAttributes",
    "PhysicsManagerAttributes",
    "StageAttributes",
    "UVSpherePrimitiveAttributes",
]
