#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name = "sem6120-tsp",
    version = "0.1",
    author = "Alexander D Brown",
    author_email = "alex@alexanderdbrown.com",
    url = "",
    description = "",
    long_description = "open('README.md').read()",

    # Packages
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    
    entry_points = {
        'console_scripts': [
            'sem6120-tsp=tsp:main',
        ]    
    },

    # Requirements
    install_requires = [
      'psutil',
    ],

)
