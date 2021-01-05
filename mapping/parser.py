import argparse


__all__ = ["parser"]


def parser():
    
    description = "Map chinese characters to their stroke order"
    parser = argparse.ArgumentParser(description=description,
                                    formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=35))

    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('-c', '--chars', type=lambda s: unicode(s, 'utf8'),
                        help='string with characters to map', metavar='str')

    input_group.add_argument('-f', '--file', type=str, metavar='filename',
                    default='list.txt', 
                    help="file with characters to map. Default: list.txt")

    options_group = parser.add_mutually_exclusive_group()
    options_group.add_argument('-v','--verbose', action='store_true', help='see you progress')
    options_group.add_argument('-q','--quiet', action='store_true', help='hide all outputs')

    parser.add_argument('-o', '--open', nargs ='?', default=None, const="zdict", metavar='url', type=str,
                        help="open the dictionary passed as argument on the character to be mapped. Default: zdict")
    parser.add_argument('--env', action='store_true', help="create a working environment with all the files "
                        "and directories the script uses to map characters and exit")

    return parser.parse_args()
