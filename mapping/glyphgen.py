import os
import fontforge as ff
from .pathutils import *

__all__ = ["generate_glyphs"]


def generate_glyphs(glyph_list):
    """
        Generate .svg in glyphs/raw for all the glyphs passed as argument and return
        their file names as a list

    Parameters
    ----------
    glyph_list : list of str
        List of the glyphs' fontforge unicode respresentation 

    Returns
    -------
    list of str
        List of the filenames of the generated glyphs

    Raises
    ------
    EnvironmentError
        If the fontforge module cannot open the font defined in FONT_NAME
    """

    try:
        font = ff.open(FONT_NAME)
    except:
        raise EnvironmentError(" \'{}\' in \'{}\' is probably corrupt, try to download it again."
                        .format(FONT_NAME, os.path.abspath(os.getcwd())))

    os.chdir(raw_path)
    glyph_flist = ['']*len(glyph_list)

    for glyph in font:
        if font[glyph].glyphname in glyph_list:

            if font[glyph].isWorthOutputting():
                filename = font[glyph].glyphname + ".svg"
                font[glyph].export(filename)

                idx = glyph_list.index(font[glyph].glyphname)
                glyph_flist[idx] = filename
    return glyph_flist
