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
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='A letter')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    for letter in args.letter:
        print(letter)
    lookup = {}
    for line in args.file:
        print(line[0], end='')
        lookup[line[0]] = line.rstrip()
    print()
    print(lookup['A'])
    print(lookup['Z'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
