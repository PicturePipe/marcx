#!/usr/bin/env python

""" 
marcx consists mainly of a `pymarc.Record` subclass called `FatRecord`,
that implements a few extra methods, which should ease MARC library
metadata manipulations.

Documentation and examples can be found under: https://github.com/miku/marcx
"""

from setuptools import setup

classifiers = """
Development Status :: 4 - Beta
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Text Processing :: General
"""

setup(name='marcx',
      version='0.1.7',
      description='MARC record manipulation library based on pymarc',
      long_description=__doc__,
      classifiers=filter(None, classifiers.split('\n')),
      author='Martin Czygan',
      author_email='martin.czygan@gmail.com',
      url='https://github.com/miku/marcx',
      py_modules=['marcx'],
      install_requires=['pymarc>=2.0', 'pyisbn>=0.6'])
