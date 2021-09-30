from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Python package ginRex"
LONG_DESCRIPTION = "Python package for grazing incidene time-resolved Exafs"


setup(
    name="ginrex",
    version=VERSION,
    author="Sebastian Paripsa",
    author_email="sebastian.paripsa@uni-wuppertal.de",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["xraylarch",],  # add any additional packages that
    # needs to be installed along with your package.
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
