"""A setuptools based setup module for fairMLHealthHealth

"""
from setuptools import setup, find_packages
import pathlib


# Set strings that should be defined elsewhere. ToDo: define elsewhere
long_description = ("A library facilitating fairness measurement" +
                    " and deployment of fairness-aware ML algorithms")


def _get_version():
    import json
    import os

    version_file = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'version.json'
    )
    return json.load(open(version_file))['version']


setup(
    name='fairMLHealth',
    version=_get_version(),
    description='Health-centered fairness measurement and management',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/KenSciResearch/fairMLHealth',
    author='KenSci',
    author_email='christine.allen@kensci.com',
    python_requires='>=3.5, <4',
    install_requires=['aif360>=0.3.0',
                      'fairlearn>=0.4.6',
                      'lightgbm',
                      'matplotlib',
                      'numpy>=1.17.2',
                      'pandas>=0.25.1',
                      'requests',
                      'scipy>=1.3.1',
                      'scikit-learn>=0.22.1',
                      'seaborn',
                      'tensorflow',
                      'xgboost'
                    ],
    project_urls={'KenSci': 'https://www.kensci.com'},
    keywords='healthcare, machine learning, fairness',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(include=['fairMLHealth', 'fairMLHealth.*'])
)
