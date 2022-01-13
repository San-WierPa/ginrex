"""
The :mod:`~ginrex.plot_exafs` module gives the following utility functions:

   * - :func:`absorption`
     - Returns Matplotlib.pyplot figure.
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import log


def absorption(filename):
    """
    Calculates the absorption according to PetraIII columns I1 and I0
    and plots a simple figure.

    Parameters
    ----------
    filename: String

    Returns
    -------
    Matplotlib.pyplot figure
    """
    datatxt = np.genfromtxt(filename)
    mu = -log(datatxt[:, 18] / datatxt[:, 17])
    plt.plot(datatxt[:, 0], mu)
    plt.show(block=False)
