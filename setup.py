# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="sample",
    version="0.0.0",
    description="Sample package",
    long_description=readme,
    author="Matthew Woods",
    author_email="mxttwoods@gmail.com",
    url="https://github.com/mxttwoods/samplemod",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
