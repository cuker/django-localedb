#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION = '0.0.1'
LONG_DESC = """\
The purpose of this package is to provide a set of localization tools that are database driven and match python locale's functionality. 
In addition, this application does not globally set any localization targets and thus aims to be thread safe and suitable for a site that needs to display different types of currencies.
"""

setup(name='django-localedb',
      version=VERSION,
      description="A django application that is a database driven version of python's locale module",
      long_description=LONG_DESC,
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Natural Language :: English',
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      keywords='django localization',
      author='Jason Kraus',
      author_email='zbyte64@gmail.com',
      maintainer = 'Jason Kraus',
      maintainer_email = 'zbyte64@gmail.com',
      url='http://github.com/cuker/django-localedb',
      license='New BSD License',
      packages=find_packages(exclude=['ez_setup', 'localedb', 'tests']),
      zip_safe=False,
      install_requires=[
        'django',
      ],
      test_suite='tests.runtests.runtests',
      )
