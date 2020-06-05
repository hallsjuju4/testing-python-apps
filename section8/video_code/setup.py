"""
For pytest:
   $ pip install -e .
   $ pytest
   collects three items / all passed
"""
from setuptools import setup, find_packages

setup(name="app", packages=find_packages())
