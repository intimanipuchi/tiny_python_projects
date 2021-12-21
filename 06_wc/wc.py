#!/usr/bin/env python3
"""
Author : Roman Koziy <koziyroman@gmail.com>
Date   : 2021-12-20
Purpose: Count lines, words and characters.
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="*",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
        help="Input file(s)",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main function"""
    args = get_args()
    #print(f"args: {args}")
    #print(type(args))
    #print(f"args.file: {args.file}")
    #print(type(args.file))
    total_lines = total_words = total_bytes = 0
    for fh in args.file:
        num_lines = num_words = num_bytes = 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
            # words = line.split()
            # for word in words:
            #     num_words += 1
            # for byte in line:
            #     num_bytes += 1
        fh.close()
        print(f"{num_lines :8}{num_words :8}{num_bytes :8} {fh.name}")
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes
    if len(args.file) > 1:
        print(f"{total_lines :8}{total_words :8}{total_bytes :8} total")


# --------------------------------------------------
if __name__ == "__main__":
    main()
