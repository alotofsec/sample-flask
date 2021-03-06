# https://pythonhosted.org/setuptools/setuptools.html

from setuptools import setup, find_packages

setup(
    name='bbs',
    version='0.1',
    packages=find_packages(),

    install_requires=[
        'Flask>=0.10.1',
        'Flask-Script>=0.5.3',
        'Flask-SQLAlchemy>=0.16',
        'SQLAlchemy>=0.8.2',
    ],
)
