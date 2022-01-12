"""
The :mod:`~ginrex.utils` module gives the following utility functions:

   * - Function
     - Description
   * - :func:`get_version`
     - Returns version of ginrex.
"""


def get_version(dependencies: bool = False) -> str:
    """
    Returns an installed version of ginrex.

    Parameters
    ----------
    dependencies
        Condition to additionally get version of
        dependencies. Default is False.

    Returns
    -------
    Printable string with a version of ginrex.

    Examples
    --------
    >>> from ginrex.utils import get_version
    >>> print(get_version(dependencies=True))
    Ginrex version      : ...
    """
    import platform

    import h5py as h5
    import lmfit as lm
    import matplotlib as mpl
    import numpy as np
    import scipy as sp

    import ginrex as grx

    libr = ("Python", "Numpy", "Scipy", "Lmfit", "H5py", "Matplotlib")
    verf = ""

    if dependencies:
        for i, lib in enumerate((platform, np, sp, lm, h5, mpl)):
            if lib == platform:
                ver = lib.python_version()
            else:
                ver = lib.__version__
            verf += "{0:20}: {1}\n".format(libr[i] + " version", ver)

    ver = grx.__version__
    verf += "{0:20}: {1}".format("Ginrex version", ver)

    return verf
