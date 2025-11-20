#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Visualization utilities for habitat_sim_api_v0_2_2."""

from typing import Any, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


def observations_to_image(observation: Any, info: Any) -> Any:
    """Convert observations to an image."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


def make_video(
    observations: List[Any],
    primary_obs: str,
    primary_obs_type: str,
    output_path: str,
    **kwargs
) -> None:
    """Create a video from observations."""
    raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = ["observations_to_image", "make_video"]
