#!#!/usr/bin/env python3

from setuptools import setup
import config

author = "Majd Alfhaily"
author_email = "majd@alfhaily.me"
url = 'https://github.com/freemanrepo/mlnem'

setup(
    name='mlnem',
    version="{config.version}".format(**locals()),
    description='A ready-to-use setup of YOLO, for the Parrot Bebop 2 drone agent',
    author=author,
    author_email=author_email,
    url=url,
    packages=['mlnem'],
    entry_points={
        'console_scripts': [
            'mlnem = mlnem.console:entry',
        ],
    }
)