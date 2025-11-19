# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Scene module for habitat_sim_api."""

from typing import Any


class SemanticCategory:
    """Semantic category for scene objects."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class SemanticLevel:
    """Semantic level in a scene."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class SemanticObject:
    """Semantic object in a scene."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class SemanticRegion:
    """Semantic region in a scene."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class SemanticScene:
    """Semantic scene representation."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = [
    "SemanticCategory",
    "SemanticLevel",
    "SemanticObject",
    "SemanticRegion",
    "SemanticScene",
]
