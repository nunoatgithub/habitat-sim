# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Metadata module for habitat_sim_api."""

from typing import Any


class MetadataMediator:
    """Mediator for managing simulation metadata."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = ["MetadataMediator"]
