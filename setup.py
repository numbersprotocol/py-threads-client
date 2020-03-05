from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-threads-client',
    version='0.0.1',
    description='Python binding of Threads V2 client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Numbers',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'base58',
        'grpcio',
        'protobuf',
    ],
    extras_require={
        'test': ['coverage'],
    },
)
