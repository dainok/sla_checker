#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sla_checker",
    version="0.0.2",
    author="Andrea Dainese",
    author_email="andrea.dainese@gmail.com",
    license="GPL-3.0-or-later",
    description="A python module that will check if two events are within a defined SLA.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dainok/sla_checker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.6",
)
