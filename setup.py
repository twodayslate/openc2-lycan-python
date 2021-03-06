#
#  The MIT License (MIT)
#
# Copyright 2019 AT&T Intellectual Property. All other rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
# AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import os
from distutils.core import setup
from setuptools import find_packages

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VERSION_FILE = os.path.join(BASE_DIR, 'openc2', 'version.py')

def get_version():
    with open(VERSION_FILE) as f:
        for line in f.readlines():
            if line.startswith('__version__'):
                version = line.split()[-1].strip('"')
                return version
        raise AttributeError("Package does not have a __version__")

setup(
    name='openc2',
    version=get_version(),
    description='Produce and consume OpenC2 JSON messages',
    author='OASIS Open Command and Control (OpenC2) Technical Committee (TC)',
    url='https://github.com/oasis-open/openc2-lycan-python',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    keywords='openc2 cyber',
    packages=find_packages(exclude=["tests"]),
    license='MIT',
    include_package_data=True,
    install_requires=[],
    extra_require={
        'stix': ['stix2']
    }
)
