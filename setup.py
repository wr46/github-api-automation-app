#!/usr/bin/env python
import setuptools
from setuptools import setup

setup(
    name="github_automation",
    version="0.2.0",
    python_requires=">=3.12",
    description="GitHub API automation app",
    author="wr46",
    url="https://github.com/",
    packages=setuptools.find_packages(exclude=["tests*", "venv*"]),
    install_requires=[
        "termcolor>=3.3.0",
        "python-dotenv>=1.2.2",
        "PyGithub>=2.8.1",
        "PyYAML>=6.0.3",
    ],
    extras_require={
        "dev": ["pytest>=9.0.2"],
    },
)
