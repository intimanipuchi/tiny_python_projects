#!/usr/bin/env python3
"""
Author : roman <roman@localhost>
Date   : 2021-12-20
Purpose: Looking items up in a dictionary
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='A letter')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    letter = args.letter
    # print(type(letter))
    fh = args.file
    #print(type(fh))
    for i in letter:
        #print(i)
        if i.lower() not in [char for char in 'abcdefghijklmnopqrstuvwxyz']:
            print(f'I do not know "{i}".')
        else:
            #print(i)
            for line in fh:
                #print(i)
                if line[0].lower() == i.lower():
                    print(line.rstrip())
                    #print(line[0])
                    #print(i)
            fh.seek(0)
    #for line in fh:
        #print(line)
        #for i in letter:
            #print(i)
            #if line[0].lower() == i.lower():
                #print(line.rstrip())
                #print(line[0])
                #print(i)
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
