import os
import re
import sys

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'dota2api',
    'dota2api.src',
    'dota2api.ref',
    'dota2api.obj',
]

author = ''
with open('dota2api/__init__.py', 'r') as fd:
    author = re.search(r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)


version = ''
with open('dota2api/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name="dota2api",
    version=version,
    author=author,
    author_email="mail@joshuaduffy.org",
    url="https://github.com/joshuaduffy/dota2api",
    description="Dota 2 API wrapper and parser",
    long_description=readme,
    license="GPL",
    keywords="dota2 dota api dota2api parser",
    packages=packages,
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