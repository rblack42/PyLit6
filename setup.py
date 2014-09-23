# -*- codeing: utf-8 -*-
"""
    setup
    ~~~~~

    distutils control file
"""
from distutils.core import setup

import pylit6.__about__ as about

setup(
    name=about.__title__,
    version=about.__version__,
    author=about.__author__,
    author_email=about.__email__,
    url=about.__url__,
    description=about.__summary__,
    scripts = ['scripts/pylit6'],
    packages = ['pylit6'],
)

