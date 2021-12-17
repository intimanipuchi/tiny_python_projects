#!/usr/bin/env python3
"""
Author : Roman Koziy <koziyroman@gmail.com>
Date   : 2021-12-16
Purpose: Working with dictionaries
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", type=str, help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    out_list = []
    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "0": "5",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
    }
    for i in text:
        # print(i)
        if i in jumper:
            out_list.append(jumper[i])
            # print(str_arg)
        else:
            out_list.append(i)
    out_text = "".join(out_list)
    print(out_text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
