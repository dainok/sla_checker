#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sla_checker",  # Replace with your own username
    version="0.0.1",
    author="Andrea Dainese",
    author_email="andrea.dainese@gmail.com",
    description="A simple package to check SLA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dainok/sla_checker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)