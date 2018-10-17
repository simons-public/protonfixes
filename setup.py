""" Install the protonfixes package
"""
import os
import glob
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

data_files = []
bin_dir = os.path.join(os.path.dirname(__file__), 'static')
for root, dirs, files in os.walk(bin_dir):
    root_files = [os.path.join(root, i) for i in files]
    data_files.append((root, root_files))

print(data_files)

setup(
    name='protonfixes',
    version='1.0.13',
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
    zip_safe=False,
    data_files = data_files,
    )
