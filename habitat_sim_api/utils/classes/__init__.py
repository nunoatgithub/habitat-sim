#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Stub classes for utils/classes package."""

from typing import Any


class MarkersetsEditor:
    """Editor for marker sets."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class SemanticDisplay:
    """Display for semantic information."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class ObjectEditor:
    """Editor for objects."""
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = ["MarkersetsEditor", "SemanticDisplay", "ObjectEditor"]
