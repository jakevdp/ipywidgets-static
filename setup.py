from distutils.core import setup

DESCRIPTION = "Jupyter static interactive figures"
LONG_DESCRIPTION = ("Generate interactive figures in Jupyter which solely depend on "
                    "JavaScript and, hence, can be exported to static HTML webpages. "
                    "Forked from https://github.com/jakevdp/ipywidgets-static")
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
      packages=['staticinteract']
      )
