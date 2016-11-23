import glob
import os

from setuptools import setup, find_packages

_dir = os.path.dirname(__file__)

setup(
    name='pyrapidparser',
    version='0.1.1',
    author='Michele Dionisio',
    author_email='michele.dionisio@gmail.com',
    url='https://github.com/jf---/pyrapidparser',

    packages=find_packages(),

    package_data = {
        '': ['*.cfg', 'bin/*.sh', 'Palletizer/*.mod', 'default/standard.sys', 'test/*.*'],
    },

    description='parse ABB RAPID code',
    long_description=open(os.path.join('pyrapidparser', 'README.md')).read(),
    install_requires=[
        "ply",
    ],
)
