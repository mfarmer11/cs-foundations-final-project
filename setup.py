#!/usr/bin/env python

from setuptools import setup, find_packages

with open('requirements.txt') as f:
	required = f.read().splitlines()

setup(name='Final-Group-Project',
      version='1.0.0',
      description='Global Economic Comparisons',
      author=['Chi Cheung', 'Fernando Zambrano', 'Galen Hancock', Manoah Farmer']
      author_email=['chicheung@gwmail.gwu.edu', 'fzambrano25@gwu.edu', 'ghancock@gwmail.gwu.edu', 'manaohf@gwu.edu']
      license='MIT'
      url='https://github.com/mfarmer11/cs-foundations-final-project.git',
      packages= find_packages(), 
      install_requires = required,
     )
