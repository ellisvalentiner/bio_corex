#!/usr/bin/env python

from distutils.core import setup

setup(name='Bio CorEx',
    version='1.0',
    description='Python Implementation of Correlation Explanation',
    author='Greg Ver Steeg',
    author_email='gregv@isi.edu',
    url='https://github.com/gregversteeg/bio_corex',
    packages=['corex', 'corex.vis'],
    install_requires=[
        'numpy>=1.8.0',
        'scipy>=0.13.0'
    ]
    )
