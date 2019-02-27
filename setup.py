import os
from setuptools import setup
import sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def conf_path(name):
  if sys.prefix == '/usr':
    conf_path = os.path.join('/etc', name)
  else:
    conf_path = os.path.join(sys.prefix, 'etc', name)
  return conf_path
setup(
    name = "ece-postprocess",
    version = "0.1",
    author = "Yang Liu, Ronald van Haren",
    author_email = "y.liu@esciencecenter.nl",
    description = ("A package for postprocessing and archiving EC-EARTH data"),
    license = "Apache 2.0",
    url = "https://github.com/blue-action/ece-postprocess",
    packages=['ece_postprocess'],
    data_files=[(os.path.join(conf_path('ece_postprocess')), ['cylc/suite.rc'])],
    scripts=['ece_postprocess/scripts/ece-postprocess'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires=['python-dateutil', 'numpy', 'netCDF4',
                      'matplotlib', 'pyproj', 'pygrib', 'configargparse',
                      'pathos'],
)
