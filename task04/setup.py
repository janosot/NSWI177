#!/usr/bin/env python3

# SPDX-License-Identifier: Apache-2.0
# Copyright 2020 Charles University

import os
from setuptools import setup

def get_readme():
    with open('README') as f:
        return f.read()

setup(
    name="matfyz-nswi177-my_ssg",
    version="0.1",
    description="Static site generator",
    long_description=get_readme(),
    classifiers=[
        "Programming Language :: Python :: 3.7", "Static site generator :: Jinja2 Template"
    ],
    keywords="site generator jinja2",
    url="https://d3s.mff.cuni.cz/teaching/nswi177/tasks/04/",
    install_requires=[
        'pyyaml', 'jinja2', 'markdown'
    ],
    include_package_data=True,
    zip_safe=False,
    packages=[
        "matfyz.nswi177"
    ],
    entry_points={
        "console_scripts" : [
            "my_ssg=matfyz.nswi177.my_ssg:main"
        ]
    },   
)
