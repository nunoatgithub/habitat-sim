# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""Sensor noise models for habitat_sim_api_v0_2_2."""

from typing import Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


class SensorNoiseModel:
    """Base class for sensor noise models."""
    
    def __call__(self, observation: Any) -> Any:
        """
        Apply noise to an observation.
        
        Args:
            observation: The clean observation
            
        Returns:
            The noisy observation
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class RedwoodDepthNoiseModel(SensorNoiseModel):
    """Depth noise model based on Redwood dataset."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class GaussianNoiseModel(SensorNoiseModel):
    """Gaussian noise model."""
    
    def __init__(self, mean: float = 0.0, std: float = 1.0):
        """
        Initialize Gaussian noise model.
        
        Args:
            mean: Mean of the Gaussian distribution
            std: Standard deviation of the Gaussian distribution
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class SaltAndPepperNoiseModel(SensorNoiseModel):
    """Salt and pepper noise model."""
    
    def __init__(self, noise_prob: float = 0.05):
        """
        Initialize salt and pepper noise model.
        
        Args:
            noise_prob: Probability of noise
        """
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class PoissonNoiseModel(SensorNoiseModel):
    """Poisson noise model."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


class SpeckleNoiseModel(SensorNoiseModel):
    """Speckle noise model."""
    
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("habitat_sim_api is an interface-only package")


def make_sensor_noise_model(name: str, config: Optional[Any] = None) -> SensorNoiseModel:
    """
    Factory function to create sensor noise models.
    
    Args:
        name: Name of the noise model
        config: Configuration for the noise model
        
    Returns:
        The noise model instance
    """
    raise NotImplementedError("habitat_sim_api is an interface-only package")


__all__ = [
    "SensorNoiseModel",
    "RedwoodDepthNoiseModel",
    "GaussianNoiseModel",
    "SaltAndPepperNoiseModel",
    "PoissonNoiseModel",
    "SpeckleNoiseModel",
    "make_sensor_noise_model",
]
