#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

install_requires = []

extras_require = {
    "test": ["pytest==3.4.0", "pytest-cov==2.5.1"],
    "dev": [
        "pip==8.1.2",
        "bumpversion==0.5.3",
        "wheel==0.29.0",
        "watchdog==0.8.3",
        "flake8==2.6.0",
        "tox==2.3.1",
        "coverage==4.1",
        "Sphinx==1.4.8",
    ]
}

setup(
    name='simple_csv_filter',
    version='0.0.1',
    description='Pure Python CSV filter with simple regex',
    long_description=readme + '\n\n' + history,
    author="Thomas blQn",
    author_email='contact__at__blqn.fr',
    url='https://github.com/blqn/simple_csv_filter',
    packages=find_packages(include=['simple_csv_filter']),
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extras_require,
    license="BSD license",
    zip_safe=False,
    keywords='simple_csv_filter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
