from __future__ import print_function
import os
from lxml import etree
from .pathutils import * 


__all__ = ["append_numbers"]


# SVG_NAMESPACE = "http://www.w3.org/2000/svg"
# XLINK_NAMESPACE = "http://www.w3.org/1999/xlink"


def append_numbers(glyph_flist):
    """
        Append the numbers to each glyphs' .svg and save them in 'glyphs/converted'

    Parameters
    ----------
    glyph_flist : list of str
        List with the names of the .svg files that the numbers will be appended to.
    """

    os.chdir(glyphs_path)

    for glyphf in glyph_flist:

        with open(raw_path + glyphf) as fid:
            svg_gly = etree.parse(fid, parser=etree.XMLParser(huge_tree=True))
            gly_root = svg_gly.getroot()

        with open(glyphs_path + NUMBERS_NAME) as fid:
            svg_num = etree.parse(fid, parser=etree.XMLParser(huge_tree=True))
            gly_root.append(svg_num.getroot())

        out = etree.tostring(
                    gly_root,
                    xml_declaration=True,
                    standalone=True,
                    pretty_print=True,
                    encoding=None,
                )

        
        with open(converted_path + glyphf, "wb") as fid:
            fid.write(out)
        
        os.remove(raw_path + glyphf)
    return
