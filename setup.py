#!/usr/bin/env python
# coding=utf-8
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name='kiki-turtle',
    version=1.3,
    description=(
        '利用链式语法包装 turtle 库，受到 schemdraw 的启发，使 turtle 绘图更符合自然语言'
    ),
    long_description=open('README.rst', encoding='utf-8').read(),
    author='langxm',
    author_email='964683112@qq.com',
    maintainer='langxm',
    maintainer_email='964683112@qq.com',
    license='GUN GPL',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/kidscodinggroup/kiki-turtle',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        
        'Topic :: Software Development :: Libraries'
    ],
)