# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Graphics-related classes and utilities."""

from typing import Any


class LightInfo:
    """Information about a light source."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class LightPositionModel:
    """Model for light positions."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class Renderer:
    """Renderer for the simulator."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class RenderCamera:
    """Camera used for rendering."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class RenderTarget:
    """Target for rendering."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = [
    "LightInfo",
    "LightPositionModel",
    "Renderer",
    "RenderCamera",
    "RenderTarget",
]
