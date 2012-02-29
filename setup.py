#!/usr/bin/env python

from setuptools import setup
import sol

try:
    longdesc = open('README.rst').read()
except Exception:
    longdesc = "Long description"

setup(
    # Metadata
    name='sol',
    version='.'.join(map(str, sol.VERSION)),
    description='',
    long_description=longdesc,
    author='Josh Bothun',
    author_email='joshbothun@gmail.com',
    classifiers=[
        'Programming Language :: Python',
    ],
    install_requires=[],

    # Program data
    # scripts=['bin/command'],
    packages=['sol'],
)
