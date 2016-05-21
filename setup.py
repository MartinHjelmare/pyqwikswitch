#!/usr/bin/env python
"""pyqwikswitch library setup"""

from setuptools import setup

setup(name='pyqwikswitch',
      version='0.2',
      description='Library to interface Qwikswitch USB Hub',
      url='https://github.com/kellerza/pyqwikswitch',
      author='Johann Kellerman',
      author_email='kellerza@gmail.com',
      license='MIT',
      packages=['pyqwikswitch'],
      install_requires=['requests'],
      zip_safe=True)
