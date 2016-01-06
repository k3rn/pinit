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
        "Flask==0.10.1",
        "Flask-User==0.6.8",
        "gunicorn==19.4.1",
        "flask-debugtoolbar==0.10.0"
    ],
)
