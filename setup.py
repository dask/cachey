#!/usr/bin/env python

from os.path import exists
from setuptools import setup

import sys
if {'pytest', 'test', 'ptr'}.intersection(sys.argv):
    setup_requires = ['pytest-runner']
else:
    setup_requires = []

setup(name='cachey',
      version='0.2.1',
      description='Caching mindful of computation/storage costs',
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
      url='http://github.com/dask/cachey/',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='',
      packages=['cachey'],
      tests_requires=['pytest'],
      install_requires=list(open('requirements.txt').read().strip().split('\n')),
      long_description=(open('README.md').read() if exists('README.md')
                        else ''),
      setup_requires=setup_requires,
      python_requires='>=3.6',
      long_description_content_type='text/markdown',
      zip_safe=False)
