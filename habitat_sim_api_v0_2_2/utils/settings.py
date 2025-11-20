#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Settings utilities for habitat_sim_api_v0_2_2."""

from typing import Any, Dict, Optional


def default_sim_settings() -> Dict[str, Any]:
    """Get default simulator settings."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def make_cfg(settings: Dict[str, Any]) -> Any:
    """Make configuration from settings dictionary."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = ["default_sim_settings", "make_cfg"]
