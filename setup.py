#!/usr/bin/env python
import os
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), 'requirements', *f)).readlines()]))

install_requires = reqs('default.txt')
tests_require = []

packages = [
    'cookiecutter_wordpress_secret',
]

dependency_links = [
    'https://github.com/aventurella/cookiecutter/tarball/dev#egg=cookiecutter-dev'
]


setup(
    name='cookiecutter_wordpress_secret',
    version='0.1.1',
    description='Cookiecutter Wordpress Secret Jinja Plugin',
    long_description=readme,
    author='Adam Venturella',
    author_email='aventurella@blitzagency.com',
    url='https://github.com/blitzagency/cookiecutter_wordpress_secret',
    packages=packages,
    package_dir={'cookiecutter_wordpress_secret': 'cookiecutter_wordpress_secret'},
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    license="BSD",
    zip_safe=False,
    keywords='cookiecutter plugin',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    tests_require=tests_require,
    test_suite='tests',

    entry_points={
        'cookiecutter.plugins.jinja': [
            'wordpress_secret = cookiecutter_wordpress_secret.plugin:WordpressSecret'
        ],
    },
)
