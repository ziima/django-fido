#!/usr/bin/python
"""Setup script for django_fido."""
from setuptools import find_packages, setup

import django_fido

INSTALL_REQUIRES = ['Django>=1.11']
EXTRAS_REQUIRE = {'quality': ['isort', 'flake8', 'pydocstyle'],
                  'test': ['mock']}

setup(name='django-fido',
      version=django_fido.__version__,
      description='Django application for FIDO protocol U2F',
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE)