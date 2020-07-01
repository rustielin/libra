# Copyright (c) The Libra Core Contributors
# SPDX-License-Identifier: Apache-2.0

from setuptools import setup, find_packages

setup(
    name="compat-net",
    version="0.1.0",
    description="tooling to compatibility test against mixed network configurations",
    python_requires=">=3.5",
    packages=find_packages(),
    tests_require=["pytest", "pytest-runner"],
    package_dir={"": "."},
    setup_requires=["pytest-runner"],
)
