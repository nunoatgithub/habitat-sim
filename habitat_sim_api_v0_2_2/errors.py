# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Error classes for habitat_sim_api_v0_2_2."""


class InvalidAttachedObject(RuntimeError):
    """Raised when an attached object is invalid."""
    pass


class GreedyFollowerError(RuntimeError):
    """Raised when greedy follower encounters an error."""
    pass


__all__ = ["InvalidAttachedObject", "GreedyFollowerError"]
