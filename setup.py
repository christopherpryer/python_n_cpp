"""http://docs.cython.org/en/latest/src/userguide/wrapping_CPlusPlus.html"""
from distutils.core import setup

from Cython.Build import cythonize

setup(ext_modules=cythonize("rect.pyx"))