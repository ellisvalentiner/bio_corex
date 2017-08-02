#!/usr/bin/env python

from setuptools import setup

setup(name='corex',
      version='1.0',
      description='Python Implementation of Correlation Explanation',
      author='Greg Ver Steeg',
      author_email='gregv@isi.edu',
      url='https://github.com/gregversteeg/bio_corex',
      install_requires=[
          'numpy>=1.8.0',
          'scipy>=0.13.0'
      ])
