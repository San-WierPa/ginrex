import clr

clr.AddReference(
    "C:\\Users\\yuli.pari\\Desktop\\gitUni\\ginRex\\ginrex\\dlls\\TREX.dll"
)

from TREX import Splitter


def counting_rows(sourcefile) -> int:
    """
    Delivers the number of rows of a given file.

    Parameters
    ----------
    sourcefile: String
        Datafile under investigation.
    """
    return Splitter.CountingRows(sourcefile)
