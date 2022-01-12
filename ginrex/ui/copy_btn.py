import pyperclip


def copied_text(filename) -> str:
    """
    Copies the last loaded datafile into the cache.

    Parameters
    ----------
    filename: String
    """
    return pyperclip.copy(filename)
