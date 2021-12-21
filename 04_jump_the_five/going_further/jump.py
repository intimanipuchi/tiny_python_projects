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
    out_text = ''
    jumper = {
        "1": " one ",
        "2": " two ",
        "3": " three ",
        "4": " four ",
        "5": " five ",
        "6": " six ",
        "7": " seven ",
        "8": " eight ",
        "9": " nine ",
        "0": " zero ",
    }
    
    for char in text:
        out_list.append(char)
    # print(out_list)
    list_length = len(out_list)
    # print(list_length)

          
    out_text = (text.translate(str.maketrans(jumper))).rstrip()
    # print(out_text + '.')
    # print(out_text.rstrip() + '.')
    out_text = " ".join(out_text.rstrip().split())
    to_list = []
    for i in out_text:
        to_list.append(i)
    if to_list[-1] not in 'abcdefghijklmnopqrstuvwxyz1234567890':
        if to_list[-2] == ' ':
            to_list.pop(-2)
    out_text = ''.join(to_list)
    print(out_text)
    """
    for i in text:
        # print(i)
        if i in jumper:
            out_list.append(jumper[i])
            # print(str_arg)
        else:
            out_list.append(i)
    out_text = "".join(out_list)
    print(out_text)
    """


# --------------------------------------------------
if __name__ == "__main__":
    main()
