#!/usr/bin/env python3
"""
Author : roman <roman@localhost>
Date   : 2021-12-21
Purpose: Rock the Casbah
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
    parser.add_argument('word',
                        metavar='word',
                        help='A word',
                        type=str)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    words_dict = {}
    
    for line in args.file:
        words = line.lower().split()
        for word in words:
            if word.lower() not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
    print(f"{args.word} was found {words_dict[args.word.lower()]} times.")
    sorted_words = sorted(words_dict.items(), key = lambda kv: kv[1], reverse = True)
    for i in range(30):
        pp(sorted_words[i])

# --------------------------------------------------
if __name__ == '__main__':
    main()
