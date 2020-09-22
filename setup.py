
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
    name='click-skeleton',
    version='0.7.0',
    description='Click app skeleton',
    python_requires='<3.9,>=3.6',
    author='Adrien Pensart',
    packages=['click_skeleton'],
    package_dir={"": "."},
    package_data={"click_skeleton": ["*.typed"]},
    install_requires=['attrdict==2.*,>=2.0.1', 'click==7.*,>=7.1.2', 'click-aliases==1.*,>=1.0.1', 'click-completion==0.*,>=0.5.0', 'click-didyoumean==0.*,>=0.0.3', 'click-help-colors==0.*,>=0.8.0', 'click-option-group==0.*,>=0.5.1', 'colorama==0.*,>=0.4.3', 'pytest==6.*,>=6.0.1', 'pytest-click==1.*,>=1.0.2', 'requests==2.*,>=2.24.0', 'semver==2.*,>=2.10.2'],
    extras_require={"dev": ["coverage-badge==1.*,>=1.0.1", "flake8==3.*,>=3.8.3", "mypy==0.*,>=0.782.0", "pylint==2.*,>=2.6.0", "pytest-cov==2.*,>=2.10.1", "pytype==2020.*,>=2020.9.16"]},
)
