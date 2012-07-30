from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.contentrules.mailadapter',
      version=version,
      description="A mail content rule action using an adapter for emails resolving",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone content rule mail adapter',
      author='Matous Hora (DMS4u)',
      author_email='matous.hora@dms4u.cz',
      url='http://pypi.python.org/pypi/collective.contentrules.mailadapter',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.contentrules'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
