"""
This module provides a class of various methods of the c# Splitter-file
from the TREX.dll.
"""

import clr

clr.AddReference(
    "C:\\Users\\yuli.pari\\Desktop\\gitUni\\ginRex\\ginrex\\dlls\\TREX.dll"
)
from TREX import Splitter


class PySplitter:
    """
    Delegates all method calls to "Splitter"-file from the TREX.dll
    """

    def __init__(self) -> None:
        self.splitter = Splitter()

    # def __getattribute__(self, __name: str) -> Any:
    #    pass

    def counting_rows(filename) -> int:
        """
        Delivers the number of rows of a given file.

        Parameters
        ----------
        filename: String
            Datafile under investigation, which is automatically copied from the
            initial loading of a datafile.
        """
        return Splitter.CountingRows(filename)
