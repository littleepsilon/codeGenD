# -*- coding:utf-8 -*-
#
# time:        19:32
# date:        2020/06/06
# description: none
# author:      david
# 

import setuptools
# try:
#     import pypandoc
#     long_description = pypandoc.convert('README.md','rst')
# except:
#     with open("README.md", "r") as fh:
#         long_description = fh.read()

setuptools.setup(
    name="codeGenD",
    version="0.0.5",
    author="David Young",
    author_email="david_young11@163.com",
    description="A tiny code generate module",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/littleepsilon/codeGenD",
    packages=setuptools.find_packages(),
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)