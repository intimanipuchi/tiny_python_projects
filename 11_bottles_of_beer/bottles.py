#!/usr/bin/env python3
"""
Author : Roman Koziy <koziyroman@gmail.com>
Date   : 2022-01-30
Purpose: Bottles of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num = args.num

    # Version 1
    # for i in range(args.num, 0, -1):
    #     print(verse(num))
    #     num -=1

    # Version 2
    # song = [verse(i) for i in reversed(range(1, num + 1))]
    # for j in song:
    #     print(j)

    # Version 3
    song = map(verse, range(num, 0, -1))
    for j in song:
        print(j)

def verse(bottle):
    """Sing a verse"""
    if bottle > 2:
        return '\n'.join([
        f'{bottle} bottles of beer on the wall,', 
        f'{bottle} bottles of beer,',
        'Take one down, pass it around,',
        f'{bottle - 1} bottles of beer on the wall!\n'
        ])
    if bottle == 2:
        return '\n'.join([
        f'{bottle} bottles of beer on the wall,', 
        f'{bottle} bottles of beer,',
        'Take one down, pass it around,',
        f'{bottle - 1} bottle of beer on the wall!\n'
        ])
    else:
        return '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
        ])

def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
       '1 bottle of beer on the wall,', '1 bottle of beer,',
       'Take one down, pass it around,',
       'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,',
        '1 bottle of beer on the wall!'
    ])

# --------------------------------------------------
if __name__ == '__main__':
    main()
