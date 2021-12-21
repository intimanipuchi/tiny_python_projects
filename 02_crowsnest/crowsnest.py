#!/usr/bin/env python3
"""
Author : Roman Koziy <koziyroman@gmail.com>
Date   : 2021-12-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='TPP Ch2. Strings.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    vowels = 'aeiou'
    if word[0] in vowels or word[0] in vowels.upper():
        article = 'an'
    else:
        article = 'a'
    print("Ahoy, Captain, {} {} off the larboard side!".format(
        article, word))

# --------------------------------------------------
if __name__ == '__main__':
    main()
