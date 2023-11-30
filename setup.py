# Copyright 2023 Fluid Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#  coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "fluid"

def load_version(filename):
    loader = SourceFileLoader(filename, filename)
    return loader.load_module().VERSION


def load_requirements(filename):
    with open(filename) as fd:
        return fd.readlines()


requirements = load_requirements("requirements.txt")
test_requirements = load_requirements("test-requirements.txt")

setup(
    name=NAME,
    description="Fluid Python SDK",
    version=load_version("fluid/version.py"),
    author="Fluid Authors",
    author_email="fluid.opensource.project@gmail.com",
    url="https://github.com/fluid-cloudnative/fluid-client-python",
    license="Apache License Version 2.0",
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    tests_require=test_requirements,
    install_requires=requirements,
    python_requires=">=3.7",
)