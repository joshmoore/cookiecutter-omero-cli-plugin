#!/usr/bin/env python
#
# Copyright (c) {% now 'utc', '%Y' %} University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
import os
import sys

from setuptools import setup


def read(fname):
    """
    Utility function to read the README file.
    :rtype : String
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


version = '0.1.0'
url = '{{ cookiecutter.github_repository_url }}'

setup(
    version=version,
    packages=['', 'omero.plugins'],
    package_dir={"": "src"},
    name='omero-{{ cookiecutter.cli_command}}',
    description='{{ cookiecutter.short_description }}',
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 '
        'or later (GPLv2+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],  # Get strings from
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    license='GPL-2.0+',
    url='%s' % url,
    zip_safe=False,
    download_url='%s/v%s.tar.gz' % (url, version),
    install_requires=[
        'omero-py>=5.8',
        'future'
    ],
    python_requires='>=3',
    keywords=['OMERO.CLI', 'plugin'],
    tests_require=[
        'pytest',
        'restview',
        'mox3'],
)

{
    "full_name": "OME Team",
    "email": "ome-team@openmicroscopy.org",
    "github_username_or_organization": "ome",
    "cli_command": "somethingshort",
    "github_repository_url": ["https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.cli_command}}", "provide later"],
    "module_name": "{{ cookiecutter.plugin_name|lower|replace('-', '_') }}",
    "short_description": "A simple plugin for accessing OMERO",
    "use_git_tags_for_versioning": "n"
}