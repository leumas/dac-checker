# -*- coding: utf-8 -*-
from ez_setup import use_setuptools
use_setuptools('0.6c9')

from setuptools import setup, find_packages


setup(name = 'dac-checker',
      version = '0.1.1',
      author= "Gustavo Lima Chaves, João Paulo Rechi Vita, "
              "Samuel Filipe Cardoso Vieira",
      description = "DAC's graduation problem solver.",
      keywords = 'python DAC unicamp',
      packages = find_packages(),
      scripts = [
        "bin/dac-checker"
        ],
      zip_safe=False,
      )
