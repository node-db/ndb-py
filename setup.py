
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import ndb

with open('README.md', 'r', 'utf-8') as fp:
    long_description = fp.read()
    
packages = ['ndb']

classifiers = [
               'Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: Apache Software License',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Topic :: Software Development :: Libraries',
               'Topic :: Utilities'
]

setup(
      name = 'ndb-py',
      version = ndb.__version__,
      author = 'Yugeng Hui',
      author_email = 'interhuiyg@163.com',
      url = 'https://github.com/node-db/ndb-py',
      packages = packages,
      description = 'Node Database for python',
      long_description = long_description,
      license = 'Apache 2.0',
      classifiers = classifiers
)
