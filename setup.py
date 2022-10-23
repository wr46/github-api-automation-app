#!/usr/bin/env python
import setuptools
from setuptools import setup

setup(
    name="github_automation",
    version="0.1.0",
    python_requires=">=3.9",
    description="GitHub API automation app",
    author="wr46",
    url="https://github.com/",
    py_modules=[],
    install_requires=[
        "termcolor",
        "python-dotenv",
        "pygithub"
    ],
)