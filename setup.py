from setuptools import setup, find_packages
import sys, os


setup(name='ringo_contact',
      version= '0.1',
      description="Contact extension for the ringo webframework",
      long_description="""""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ringo pyramid extension',
      author='',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      setup_requires=['hgtools'],
      install_requires=[
          'ringo'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [babel.extractors]
          tableconfig = ringo.lib.i18n:extract_i18n_tableconfig
          formconfig = formbar.i18n:extract_i18n_formconfig
          """,
          message_extractors = {'ringo_contact': [
                ('**.py', 'python', None),
                ('**.html', 'mako', None),
                ('**.mako', 'mako', None),
                ('**.xml', 'formconfig', None),
                ('**.json', 'tableconfig', None),
                ('static/**', 'ignore', None)]},

      )
