"""
Write a program which determines the Mth to the last element in a list.

INPUT SAMPLE:
The first argument is a path to a file. The file contains the series of space delimited characters followed by an integer. The integer represents an index in the list (1-based), one per line.

For example:
a b c d 4
e f g h 2

OUTPUT SAMPLE:
Print to stdout the Mth element from the end of the list, one per line. If the index is larger than the number of elements in the list, ignore that input.

For example:
a
g
"""
import fileinput
import re


def mth_to_last_element(m, seq):
    if m > len(seq):
        return None
    return seq[-1 * m]


def main():
    lines = [line.strip() for line in fileinput.input() if line]
    for line in lines:
        _args = re.split(r'\s+', line)
        mth = mth_to_last_element(int(_args[-1]), _args[:-1])
        if mth:
            print mth


if __name__ == '__main__':
    main()
