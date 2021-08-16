from setuptools import setup

setup(
    name="ginrex",
    version="0.1.0",
    description="Python package for grazing incidene time-resolved Exafs",
    author="Sebastian Paripsa",
    author_email="sparipsa@digon.io",
    packages=["ginrex"],
    install_requires=[
        "xraylarch",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.8.8",
    ],
)
