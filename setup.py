import os
from setuptools import setup, find_packages

setup(
    name='pinit',
    version='0.0.1',
    license='0.0.1',
    author='Mateus Kern',
    author_email="kern@mateuskern.com",
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        "Flask-SQLAlchemy==2.1",
        "Flask-Security==1.7.5",
    ],
)
