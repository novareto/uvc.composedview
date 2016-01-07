from setuptools import setup, find_packages
import os

version = '0.2.dev0'

setup(name='uvc.composedview',
      version=version,
      description="",
      long_description=u"",
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      license='ZPL',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      namespace_packages=['uvc'],
      zip_safe=False,
      install_requires=[
          'dolmen.field',
          'dolmen.view',
          'grokcore.component',
          'setuptools',
          'uvclight',
          'zope.component',
          'zope.interface',
          'zope.schema',
          ],
      )
