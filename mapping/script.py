from __future__ import print_function
from io import open
from . import *


def main():
    args = parser()

    if args.env:
        create_env()
        if not args.quiet:
            print("Environment created!")
        return
    
    check_env()

    if args.chars == None:
        with open(args.file, "r") as f:
            rawload = f.read()
            
        raw_chars, glyph_list = convert_input(rawload)
    else:
        raw_chars, glyph_list = convert_input(args.chars)

    glyphs_len = len(glyph_list)
    if args.verbose:
        print("Working on {} characters".format(glyphs_len))

    #TODO: Check if there are glyphs on glyphs/raw and work on them before generating new ones
    glyphs_flist = generate_glyphs(glyph_list)


    if args.verbose:
        print("{} .svg files generated for {} characters".format(len(glyphs_flist), glyphs_len))

    append_numbers(glyphs_flist)

    done_glyphs = manual_map(glyphs_flist, raw_chars, args.open, args.verbose)

    final_check(glyphs_flist, done_glyphs, args.quiet)

