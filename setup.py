#!/usr/bin/env python

import os
from setuptools import setup, find_packages

from morinkit import __version__, __author__, __license__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

url = 'https://github.com/morinlab/morinkit'
long_desc = 'For more information, visit the GitHub repository: {}'.format(url)

requires = read('requirements.txt').rstrip().split("\n")
tests_requires = read('requirements-tests.txt').rstrip().split("\n")


setup(
    name='morinkit',
    version=__version__,
    description='Python functions and scripts for genomics',
    long_description=long_desc,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Bio-Informatics'],
    keywords='bioinformatics cancer genomics utility tool',
    author=__author__,
    author_email='morinlab@sfu.ca',
    url=url,
    license=__license__,
    packages=find_packages(exclude=["tests"]),
    entry_points={'console_scripts': ['morinkit = morinkit.morinkit:main']},
    install_requires=requires,
    test_suite='tests',
    tests_require=tests_requires)
