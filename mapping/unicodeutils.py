


__all__ = ["to_ffuni", "convert_input"]


def to_ffuni(char):
    """
        Format python styled unicode to fontforge styled unicode.

    Parameters
    ----------
    char : str
        Unicode character to be converted

    Returns
    -------
    str
        fontforge styled unicode character
    """

    # TODO: Only convert chinese characters, ignore all others

    return "uni" + (hex(ord(char))[2:]).upper()



def convert_input(inp):
    """
        Convert the input characters to a list of glyph in fontforge styled unicode.
        Returns both the sanityzed raw characters and the unicode list.

    Parameters
    ----------
    inp : list of str
        Characters to be converted

    Returns
    -------
    tuple->(list, list)
        Raw sanitized characters on the first position of the tuple.
        Characters converted to fontforge styled unicode on the second
        position of the tuple.

    Raises
    ------
    ValueError
        No valid characters where found on the input.
    """

    raw = inp.replace(" ", "").replace("\n", "").replace("\t", "")

    if len(raw) == 0:
        raise ValueError("No characters found!")

    return raw, list(map(to_ffuni, raw))