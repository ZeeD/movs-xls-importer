from setuptools import find_packages
from setuptools import setup

setup(name='movs-xls-importer',
      version='0.0.1',
      author='Vito De Tullio',
      author_email='vito.detullio@gmail.com',
      description='import xls',
      url='https://github.com/ZeeD/movs-xls-importer',
      packages=find_packages(),
      python_requires='>=3.8',
      entry_points={
          'console_scripts': [
              'movs-xls-importer = movsxlsimporter.main:main'
          ]
      },
      install_requires=[
          'movs',
          'pylightxl'
      ],
      package_data={
      })
