# Copyright (c) Aaron Gallagher <_@habnab.it>
# See COPYING for details.

from __future__ import print_function

from distutils.command.build_ext import build_ext
import sys

from setuptools import Extension, setup


speedups = Extension('theseus._cytracer', [])
ext_modules = [speedups]
speedups.sources.append('theseus/_cytracer.c')


with open('README.rst', 'r') as infile:
    long_description = infile.read()


setup(
    name='twisted-theseus',
    version='0.14.1.2',
    description='a Deferred-aware profiler for Twisted',
    long_description=long_description,
    author='Aaron Gallagher',
    author_email='_@habnab.it',
    url='https://github.com/flowroute/twisted-theseus',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Twisted',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
    ],
    license='ISC',

    packages=['theseus', 'theseus.test'],
    ext_modules=ext_modules,
    setup_requires=[],
    install_requires=['Twisted'],
    cmdclass=dict(build_ext=build_ext),
    zip_safe=False,
)
