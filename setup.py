##############################################################################
#
# Copyright (c) 2008-2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup"""

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name = 'z3c.locales',
    version = '0.2.0',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    description = "Shared z3c domain translations",
    long_description=(
        read('README.txt')
        + '\n\n' +
        read('CHANGES.txt')
        ),
    keywords = "Zope z3c locale locales i18n internationalisation",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Natural Language :: German',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
    url='http://pypi.python.org/pypi/z3c.locales',
    license='ZPL 2.1',
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = ['z3c'],
    extras_require=dict(
        test=[
            'zope.testing',
            ],
        extract = [
            'z3c.authviewlet',
            'z3c.contents',
            'z3c.csvvocabulary',
            'z3c.layer.pagelet',
            'z3c.table',
            'z3c.wizard',
            ],
        ),
    install_requires = [
        'setuptools',
        'zope.i18n',
        ],
    zip_safe = False,
    )
