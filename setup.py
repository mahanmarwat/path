import os.path

from setuptools import setup
from path import __version__

setup(name='path',
      version=__version__,
      author='Mahan Marwat',
      author_email='mahanmarwat@gmail.com',
      url='https://github.com/mahanmarwat/path',
      download_url='',
      license='MIT',
      description='Intelligent Path Module for Pretty People',
      long_description=open('README.rst').read(),
      keywords='os path unipath pathlib http url',
      py_modules=['path'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ]
      )
