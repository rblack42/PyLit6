# -*- codeing: utf-8 -*-
"""
    setup
    ~~~~~

    distutils setup file
"""
from distutils.core import setup

about = {}
with open('pylit6/__about__.py') as a:
    exec(a.read(), about)

setup(
    name=about[__title__'],
    version=about[__version__'],
    description=about['__summary__'],
    long_description=README + '\n\n' + CHANGES,
    author=about['__author__'],
    author_email=about['__email__'],
    url=about['__url__'],
    packages=find_packages(),
    install_requires=[
        'grako==2.0.0',
    ]
    entry_points = {
        'console_scripts': ['pylit6=pylit6.command_line:main'],
    }
)

