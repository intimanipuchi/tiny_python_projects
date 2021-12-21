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
        description="Working with lists",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("items",
                        type=str,
                        nargs="+",
                        metavar="str",
                        help="item(s) to bring")

    parser.add_argument("-s",
                        "--sorted",
                        help="sort the list",
                        action="store_true")

    parser.add_argument("-c",
                        "--comma",
                        help="remove the Oxford comma",
                        action="store_true")

    parser.add_argument(
        "-d",
        "--delimiter",
        help="choose delimiter",
        type=str,
        metavar="str",
        default=",",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main function: formatting and printing the output"""

    args = get_args()
    sort_flag = args.sorted
    items = args.items
    delim = args.delimiter + " "
    if sort_flag:
        items = sorted(items)
    if len(items) == 1:
        print(f"You are bringing {items[0]}.")
    elif len(items) < 3:
        items.insert(-1, "and")
        print(f"You are bringing {' '.join(items)}.")
    else:
        if args.comma:
            # print(args.comma)
            end = items[-2] + " and " + items[-1]
            items.pop()
            items[-1] = end
            # print("You are bringing {}.".format(" {delim".joint(items))
        else:
            # print(items)
            last = items[-1]
            and_last = "and " + last
            items[-1] = and_last
        # print(items)
        print(f"You are bringing {delim.join(items)}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
