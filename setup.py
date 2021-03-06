#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import sys
import codecs
from setuptools import setup, find_packages
from ip138 import __version__, __author__, __email__

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]


def long_description():
    with codecs.open('README.rst', 'rb') as readme:
        if not sys.version_info < (3, 0, 0):
            return readme.read().decode('utf-8')


setup(
    name='ip138',
    version=__version__,
    author='KellyHwong',
    author_email='dianhuangkan@gmail.com',
    description='ip138.com comics downloader',
    long_description=long_description(),
    keywords=['ip138', 'comics'],
    maintainer='KellyHwong',
    maintainer_email='dianhuangkan@gmail.com',
    license='MIT',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/KellyHwong/ip138',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'ip138 = ip138.command:main',
        ]
    },
)
