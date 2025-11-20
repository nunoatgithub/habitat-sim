#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Registry for habitat_sim_api_v0_2_2.

The registry is a central source of truth for registering control functions,
noise models, and other pluggable components.
"""

import collections
from typing import DefaultDict, Optional, Type

__all__ = ["registry"]


class _Registry:
    """
    Registry for habitat_sim - a central source of truth.
    
    The registry maintains mappings of various information to unique keys.
    Special functions can be used as decorators to register different classes.
    """
    
    _mapping: DefaultDict[str, dict] = collections.defaultdict(dict)
    
    @classmethod
    def register_move_fn(
        cls,
        controller: Optional[Type] = None,
        *,
        name: Optional[str] = None,
        body_action: Optional[bool] = None,
    ):
        """
        Register a new control function.
        
        Args:
            controller: The controller class to register
            name: Name to register the control with
            body_action: Whether this action manipulates the agent's body
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    @classmethod
    def register_noise_model(
        cls, noise_model: Optional[Type] = None, *, name: Optional[str] = None
    ):
        """
        Register a new sensor noise model.
        
        Args:
            noise_model: The noise model class to register
            name: Name to register the noise model with
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    @classmethod
    def get_move_fn(cls, name: str):
        """
        Get a registered control function by name.
        
        Args:
            name: Name of the control function
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")
    
    @classmethod
    def get_noise_model(cls, name: str):
        """
        Get a registered noise model by name.
        
        Args:
            name: Name of the noise model
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")


# Global registry instance
registry = _Registry()
