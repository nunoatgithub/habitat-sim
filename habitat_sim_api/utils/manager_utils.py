#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Manager utilities for habitat_sim_api."""

from typing import Any


def get_rigid_object_manager(sim: Any) -> Any:
    """Get the rigid object manager from a simulator."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def get_articulated_object_manager(sim: Any) -> Any:
    """Get the articulated object manager from a simulator."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = ["get_rigid_object_manager", "get_articulated_object_manager"]
