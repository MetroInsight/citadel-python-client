#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'Jason Koh, MetroInsight Team'
__version__ = '0.1'

setup(
    name = 'python-citadel',
    version = __version__,
    packages = ['citadel'],
    author = __author__,
    description = 'A Python wrapper around Citadel AIP',
    zip_safe = False,
    install_requires = ['setuptools', 'requests', ],
    include_package_data = True,
    classifiers = (
        'Development Status :: 1 - Planning'
        'Intended Audience :: Developers',
    ),
    #test_suite='building_depot_test.suite',
)
