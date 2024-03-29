# -*- coding: utf-8 -*-
"""Installer for the kraeks.plonetraining package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='kraeks.plonetraining',
    version='1.0a1',
    description="internal Plone training",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone CMS',
    author='Lars Walther',
    author_email='lars.walther@educorvi.de',
    url='https://github.com/collective/kraeks.plonetraining',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/kraeks.plonetraining',
        'Source': 'https://github.com/collective/kraeks.plonetraining',
        'Tracker': 'https://github.com/collective/kraeks.plonetraining/issues',
        # 'Documentation': 'https://kraeks.plonetraining.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['kraeks'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'plone.api',
        'plone.restapi',
        'plone.app.relationfield',
        'plone.app.lockingbehavior',
        'plone.schema',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = kraeks.plonetraining.locales.update:update_locale
    """,
)
