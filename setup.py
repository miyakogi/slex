#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='slex',
    version='0.0.1',
    description='Simple and flexible sphinx theme for the flexbox age',
    long_description=readme,
    author='Hiroyuki Takagi',
    author_email='miyako.dev@gmail.com',
    url='https://github.com/miyakogi/slex',
    packages=['slex'],
    include_package_data=True,
    entry_points={
        'sphinx_themes': [
            'path = slex:get_path',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
