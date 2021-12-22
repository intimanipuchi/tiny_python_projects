#!/usr/bin/env python3
"""
Author : roman <roman@localhost>
Date   : 2021-12-21
Purpose: Count letters in a file.
"""

import argparse
from pprint import pprint as pp

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)
    parser.add_argument('letter',
                        metavar='letter',
                        help='A letter',
                        type=str)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    letters_dict = {}
    
    for line in args.file:
        letters = list(line.lower().strip())
        for letter in letters:
            if letter not in letters_dict:
                letters_dict[letter] = 1
            else:
                letters_dict[letter] += 1
    print(f"{args.letter} was found {letters_dict[args.letter]} times.")
    sorted_letters = sorted(letters_dict.items(), key = lambda kv: kv[1], reverse = True)
    pp(sorted_letters)

# --------------------------------------------------
if __name__ == '__main__':
    main()
