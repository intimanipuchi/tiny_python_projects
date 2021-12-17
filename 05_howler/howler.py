#!/usr/bin/env python3
"""
Author : Roman Koziy <koziyroman@gmail.com>
Date   : 2021-12-17
Purpose: Working with files
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        type=str,
                        metavar='text',
                        help='Input string of file',)

    parser.add_argument('-o',
                        '--outfile',
                        type=str,
                        metavar='str',
                        help='Output filename',
                        default='',)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    outfile = args.outfile
    
    if os.path.isfile(text):
        fh_in = open(text)
        text = fh_in.read()

    if outfile:
        if not os.path.isfile(outfile):
            fh_out = open(outfile, "wt")
            print(text.upper(), file=fh_out)
    else:
        print(text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
