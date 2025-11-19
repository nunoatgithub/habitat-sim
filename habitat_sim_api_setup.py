#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
Setup script for habitat-sim-api - Interface-only package.
"""

from setuptools import setup, find_packages
import os

# Read version from __init__.py
version = "0.3.3"

# Read the README
readme_path = os.path.join(os.path.dirname(__file__), "habitat_sim_api", "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = "Interface-only package mirroring habitat-sim Python API"

setup(
    name="habitat-sim-api",
    version=version,
    description="Interface-only package mirroring habitat-sim Python API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Meta Platforms, Inc.",
    license="MIT",
    url="https://github.com/facebookresearch/habitat-sim",
    packages=find_packages(include=["habitat_sim_api*"]),
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="robotics simulation embodied-ai interface",
    project_urls={
        "Homepage": "https://github.com/facebookresearch/habitat-sim",
        "Documentation": "https://aihabitat.org/docs/habitat-sim/",
        "Repository": "https://github.com/facebookresearch/habitat-sim",
    },
)
