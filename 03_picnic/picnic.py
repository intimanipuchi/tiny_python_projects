#!/usr/bin/env python3
"""
Author : Roman Koziy <koziyroman@gmail.com>
Date   : 2021-12-15
Purpose: Working with lists
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Working with lists',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        type=str,
                        nargs='+',
                        metavar='str',
                        help='item(s) to bring')

    parser.add_argument('-s',
                        '--sort',
                        help='a boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    flag_arg = args.sort
    pos_arg = args.item

    print("End of main")


# --------------------------------------------------
if __name__ == '__main__':
    main()
