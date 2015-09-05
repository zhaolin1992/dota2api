#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name="dota2api",
    version="2.0.0",
    author="Joshua Duffy, Evaldo Bratti",
    author_email="mail@joshuaduffy.org",
    url="https://github.com/joshuaduffy/dota2api",
    description="Dota 2 API wrapper and parser",
    license="GPL",
    keywords="dota2 dota api dota2api parser",
    packages=['dota2api', 'dota2api.src', 'dota2api.ref', 'dota2api.obj'],
    package_data={'dota2api.ref': ['abilities.json',
                                   'heroes.json',
                                   'items.json',
                                   'lobbies.json',
                                   'modes.json',
                                   'regions.json']},
    install_requires=['requests'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)