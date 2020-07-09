
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='ansible-builder',
    version='0.1.0',
    python_requires='==3.*,>=3.6.0',
    author='Matthew Jones',
    author_email='matburt@redhat.com',
    maintainer='Shane McDonald',
    maintainer_email='shanemcd@redhat.com',
    entry_points={"console_scripts": ["ansible-builder = ansible_builder.cli:run"]},
    packages=['ansible_builder'],
    package_dir={"": "."},
    package_data={},
    install_requires=['pyyaml==3.*,>=3.12.0'],
    extras_require={"dev": ["black==19.*,>=19.10.0.b0", "dephell==0.*,>=0.8.3", "flake8==3.*,>=3.7.9", "ipdb==0.*,>=0.13.2", "pylint==2.*,>=2.4.4", "pyparsing==2.*,>=2.4.5", "pytest==5.*,>=5.2.0", "sphinx==2.*,>=2.4.4", "tox==3.*,>=3.14.5", "yamllint==1.*,>=1.20.0"]},
)