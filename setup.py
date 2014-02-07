from setuptools import setup, find_packages
import os

version = '0.1'

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
          'grokcore.chameleon',
          'grokcore.component',
          'grokcore.view',
          'megrok.layout',
          'setuptools',
          'zope.component',
          'zope.interface',
          'zope.publisher',
          'zope.schema',
          ],
      )
