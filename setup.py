#!/usr/bin/env python
import CSVLibrary
from os.path import join, dirname, abspath
from setuptools import setup

version_file = join(dirname(abspath(__file__)), 'CSVLibrary', 'version.py')

with open(version_file) as file:
      code = compile(file.read(), version_file, 'exec')
      exec(code)

DESCRIPTION = """
CSV file support for Robot Framework. Updated to Python 3.
"""[1:-1]

setup(name         = 'robotframework-csvlibrary',
      version      = CSVLibrary.VERSION,
      description  = 'CSV library for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'Marcin Mierzejewski',
      author_email = '<mmierz@gmail.com>',
      url          = 'https://github.com/teelicht/robotframework-CSVLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing csv',
      platforms    = 'any',
      classifiers  = [
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing"
      ],
      install_requires = [
          'robotframework >= 3.0.2',
      ],
      packages    = ['CSVLibrary'],
      )
