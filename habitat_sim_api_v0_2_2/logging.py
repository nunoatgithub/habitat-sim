# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Logging utilities for habitat_sim_api_v0_2_2."""

import logging


class LoggingContext:
    """Context manager for logging configuration."""
    
    @staticmethod
    def reinitialize_from_env():
        """Reinitialize logging from environment variables."""
        pass  # No-op in interface-only version


# Create a default logger
logger = logging.getLogger("habitat_sim_api")


__all__ = ["LoggingContext", "logger"]
