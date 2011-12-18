from setuptools import setup, find_packages
import sys, os

version = '0.0'
requires = ["pyramid<=1.0"]
setup(name='brocab',
      version=version,
      description="brocabulary website",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Tom Willis',
      author_email='tom@batterii.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
