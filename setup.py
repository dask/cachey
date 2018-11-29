#!/usr/bin/env python

from os.path import exists
from setuptools import setup

import sys
if {'pytest', 'test', 'ptr'}.intersection(sys.argv):
    setup_requires = ['pytest-runner']
else:
    setup_requires = []

setup(name='cachey',
      version='0.1.1',
      description='Caching mindful of computation/storage costs',
      url='http://github.com/blaze/cachey/',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='',
      packages=['cachey', 'cachey.tests'],
      tests_requires=['pytest'],
      install_requires=list(open('requirements.txt').read().strip().split('\n')),
      long_description=(open('README.md').read() if exists('README.md')
                        else ''),
      setup_requires=setup_requires,
      zip_safe=False)
