# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Attributes managers for habitat_sim_api_v0_2_2."""

from typing import Any


class AOAttributesManager:
    """Manager for articulated object attributes."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class AssetAttributesManager:
    """Manager for asset attributes."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class LightLayoutAttributesManager:
    """Manager for light layout attributes."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ObjectAttributesManager:
    """Manager for object attributes."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class PhysicsAttributesManager:
    """Manager for physics attributes."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class SceneDatasetAttributesManager:
    """Manager for scene dataset attributes."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class StageAttributesManager:
    """Manager for stage attributes."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = [
    "AOAttributesManager",
    "AssetAttributesManager",
    "LightLayoutAttributesManager",
    "ObjectAttributesManager",
    "PhysicsAttributesManager",
    "SceneDatasetAttributesManager",
    "StageAttributesManager",
]
