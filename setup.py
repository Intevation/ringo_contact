from setuptools import setup, find_packages
import sys, os

# Major release
increment_version = "0.1"
# Minor/Bugfix release
#increment_version = "0.0.1"


setup(name='ringo_contact',
      use_vcs_version= {"increment": increment_version},
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
