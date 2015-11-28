# -*- coding: utf-8 -*-
import os
from setuptools import setup


def read(fname):
    """ Return file content. """

    return open(
        os.path.join(
            os.path.dirname(__file__), fname)
        ).read()

setup(
    name='django-elephant',
    license='MIT',
    version='0.0.1',
    install_requires=['Django'],
    url='https://github.com/jairhenrique/django-elephant',
    author='Jair Henrique',
    author_email='jair.henrique@gmail.com',
    keywords='django cache',
    description='A simple cache for Django functions and methods',
    long_description=read('README.md'),
    packages=['elephant'],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
