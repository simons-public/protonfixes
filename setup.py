""" Install the protonfixes package
"""
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='protonfixes',
    version='1.0.2',
    description='Python module for applying fixes at runtime for games not supported by Steam Proton',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/simons-public/protonfixes',
    author='Chris Simons',
    author_email='chris@simonsmail.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Games/Entertainment',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: BSD License',
        ],
    keywords='proton steam winetricks protonfixes',
    packages=find_packages(),
    )

