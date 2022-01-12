#!/usr/bin/env python3
"""
Author : Roman Koziy <koziyroman@gmail.com>
Date   : 2021-12-21
Purpose: Substitute the vowels. TPP Ch 8.
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        type=str,
                        default='a',
                        choices='aeiou')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main program"""

    args = get_args()
    #print(args)
    vowels = 'aeiou'
    vowels_upper = 'AEIOU'

    if os.path.isfile(args.text):
        fh = open(args.text)
        #print(type(fh))
        for line in fh:
            line = line.rstrip()
            for i in vowels:
                out_text = line.replace(i, args.vowel)
                line = out_text
            for j in vowels_upper:
                out_text = line.replace(j, args.vowel.upper())
                line = out_text
            print(line)
    else:
        for i in vowels:
            out_text = args.text.replace(i, args.vowel)
            args.text = out_text
        for j in vowels_upper:
            out_text = args.text.replace(j, args.vowel.upper())
            args.text = out_text
        print(out_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
