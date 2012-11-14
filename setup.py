# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='springpython-batch',
    version='0.0.1',
    description='Python implementation of core functionality of Spring Batch',
    long_description=readme,
    author='Mike McCallister',
    author_email='mike@mccllstr.com',
    url='https://github.com/mikemccllstr/springpython-batch',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

