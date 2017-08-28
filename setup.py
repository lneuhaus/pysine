# note to the developer
# do not forget to make source distribution with
# python setup.py sdist

# much of the code here is from
# https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/

#! /usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from distutils.core import setup
import io
import codecs
import os
import sys

# path to the directory that contains the setup.py script
SETUP_PATH = os.path.dirname(os.path.abspath(__file__))

def read(fname):
    return open(os.path.join(SETUP_PATH, fname)).read()

# Version info -- read without importing
_locals = {}
exec(read(os.path.join('pysine', '_version.py')), None, _locals)
version = _locals['__version__']

# # read requirements
# # from http://stackoverflow.com/questions/14399534/how-can-i-reference-requirements-txt-for-the-install-requires-kwarg-in-setuptool
# requirements = []
# here = os.path.abspath(os.path.dirname(__file__))
# with open(os.path.join(here, 'requirements.txt')) as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.strip()
#         if '#' not in line and line:
#             requirements.append(line.strip())
requirements = ['pyaudio',
                'numpy',
                'nose>=1.0']
if sys.version_info >= (3,4):  # python version dependencies
    requirements += []  # mock is part of unittest is part of standard library
else:  # python 2.7
    requirements += ['mock']

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except:
    try:
        long_description = read('README.rst')
    except:
        long_description = read('README.md')


def find_packages():
    """
    Simple function to find all modules under the current folder.
    """
    modules = []
    for dirpath, _, filenames in os.walk(os.path.join(SETUP_PATH, "pysine")):
        if "__init__.py" in filenames:
            modules.append(os.path.relpath(dirpath, SETUP_PATH))
    return [module.replace(os.sep, ".") for module in modules]


setup(name='pysine',
      version=version,
      description='Allows to play single tones on the PyAudio sound output in real time',
      long_description=long_description,
      author='Leonhard Neuhaus',
      author_email='leonhard.neuhaus@gmail.com',
      url='http://www.github.com/lneuhaus/pysine',
      license='GPLv3',
      classifiers=['Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Natural Language :: English',
                   'Development Status :: 4 - Beta',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Topic :: Scientific/Engineering :: Human Machine Interfaces'],
      keywords='sound PyAudio sine wave output play',
      platforms='any',
      packages=find_packages(),
      package_data={'pysine': []},
      install_requires=requirements,
      # what were the others for? dont remember..
      #setup_requires=requirements,
      #requires=requirements,
      # stuff for unitary test with pytest
      tests_require=['nose>=1.0'],
      # extras_require={'testing': ['pytest']},
	  test_suite='nose.collector',
      # install options
      cmdclass={}
      )
