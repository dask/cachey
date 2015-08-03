#!/usr/bin/env python

from os.path import exists
from setuptools import setup

setup(name='cachey',
      version='0.0.3',
      description='Caching mindful of computation/storage costs',
      url='http://github.com/mrocklin/cachey/',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='',
      packages=['cachey'],
      install_requires=list(open('requirements.txt').read().strip().split('\n')),
      long_description=(open('README.md').read() if exists('README.md')
                        else ''),
      zip_safe=False)
