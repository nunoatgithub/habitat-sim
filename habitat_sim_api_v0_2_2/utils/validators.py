#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Validator utilities for habitat_sim_api_v0_2_2."""

from typing import Any


class NoAttrValidationContext:
    """Context manager to disable attribute validation."""
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def all_is_finite(instance, attribute, value):
    """Validator that checks if all values are finite."""
    pass  # No-op in interface-only version


def is_unit_length(instance, attribute, value):
    """Validator that checks if value has unit length."""
    pass  # No-op in interface-only version


def value_is_validated(instance):
    """Check if a value is validated."""
    pass  # No-op in interface-only version


__all__ = [
    "NoAttrValidationContext",
    "all_is_finite",
    "is_unit_length",
    "value_is_validated",
]
