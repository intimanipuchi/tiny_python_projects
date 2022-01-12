#!/usr/bin/env python3
"""
Author : roman <roman@localhost>
Date   : 2021-12-20
Purpose: Looking items up in a dictionary
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Creating lookup dictionary",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("letter",
                        metavar="letter",
                        nargs="+",
                        type=str,
                        help="Letter(s)")

    parser.add_argument(
        "-f",
        "--file",
        help="A readable file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main program"""
    args = get_args()

    #    lookup = {}
    #    for line in args.file:
    #        lookup[line[0].upper()] = line.rstrip()
    #    Or use dictionary comprehension instead of code above
    lookup = {line[0].upper(): line.rstrip() for line in args.file}

    for letter in args.letter:
        #        if letter.upper() in lookup:
        #            print(lookup[letter.upper()])
        #        else:
        #            print(f'I do not know "{letter}".')
        print(lookup.get(letter.upper(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == "__main__":
    main()
