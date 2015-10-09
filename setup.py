#!/usr/bin/env python

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mkpasswd',
    version='1.1',
    author='Thom Dixon',
    author_email='thom@thomdixon.org',
    description=('A CLI tool and module for generating random passwords'),
    long_description=read('README.md'),
    entry_points={
        'console_scripts': ['mkpasswd-py=mkpasswd:main']
    },
    packages=['mkpasswd'],
    zip_safe=False
)
