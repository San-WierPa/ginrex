from setuptools import find_packages, setup

CLASSIFIERS = """\
LICENSE :: OSI Approved
"Programming Language :: Python :: 3"
"Intended Audience :: Science/Research"
"Operating System :: OS Independent"
"Development Status :: 1 - Development"
"""

DISTNAME = "ginRex"
VERSION = "0.1.0"
ISRELEASED = False
DESCRIPTION = "Python package ginRex"
LONG_DESCRIPTION = "Python package for grazing incidene time-resolved Exafs"
LICENSE = "MIT"
AUTHOR = "Sebastian Paripsa"
AUTHOR_EMAIL = "sebastian.paripsa@uni-wuppertal.de"

# PYTHON_REQUIRES = "3"

# INSTALL_REQUIRES = [
# "numpy",  # "xraylarch", # add any additional packages that
# needs to be installed along with your package.
# ]

PACKAGES = find_packages

metadata = dict(
    name=DISTNAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    # python_requires=PYTHON_REQUIRES,
    # install_requires=INSTALL_REQUIRES,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[CLASSIFIERS],
    license=LICENSE,
)


def setup_package() -> None:
    setup(**metadata)


if __name__ == "__main__":
    setup_package()
