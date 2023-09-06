# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lsv/__init__.py
from lsv import __version__ as version

setup(
	name="lsv",
	version=version,
	description="LSV Company",
	author="SHRDC",
	author_email="SHRDC@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
