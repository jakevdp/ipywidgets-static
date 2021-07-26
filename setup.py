from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

DESCRIPTION = "Jupyter static interactive figures"
LONG_DESCRIPTION=long_description,
LONG_DESCRIPTION_CONTENT_TYPE='text/markdown'
NAME = "staticinteract"
AUTHOR = "Semidan Robaina, Jake VanderPlas"
AUTHOR_EMAIL = "srobaina@ull.edu.es"
MAINTAINER = "Semidan Robaina"
MAINTAINER_EMAIL = "srobaina@gmail.com"
DOWNLOAD_URL = 'http://github.com/robaina/staticInteract'
LICENSE = 'BSD'

VERSION = '0.0.1'

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url=DOWNLOAD_URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['staticinteract'],
      install_requires=['matplotlib', 'numpy', 'ipython']
      )
