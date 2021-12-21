#!/usr/bin/env python3
"""
Author : Roman Koziy <koziyroman@gmail.com>
Date   : 2021-12-20
Purpose: Count lines, words and characters.
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main function"""


# --------------------------------------------------
if __name__ == '__main__':
    main()
