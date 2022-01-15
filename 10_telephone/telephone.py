#!/usr/bin/env python3
"""
Author : Roman Koziy <koziyroman@gmail.com>
Date   : 2022-01-15
Purpose: Replace characters of a string
"""

import argparse
import os
import string
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Replace characters of a string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)
    
    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text) as filehandle:
            args.text = filehandle.read().rstrip()
            # print(args.text)
    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Replace random characters"""

    args = get_args()

    random.seed(args.seed)

    text = args.text
    alpha = "".join(sorted(string.ascii_letters + string.punctuation))
    new_text = ""
    num_mutations = round(len(text) * args.mutations)
    indexes = random.sample(range(len(text)), num_mutations)
    new_text = text

#    if indexes:
#        for i in indexes:
#            new_text = text[:i] + random.choice(alpha.replace(text[i], '')) + text[i+1:]
#            text = new_text
#    else:
#        new_text = args.text
#
    for i in indexes:
        new_char = random.choice(alpha.replace(text[i], ''))
        new_text = new_text[:i] + new_char + new_text[i+1:]
    print(f'You said: "{args.text}"\nI heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
