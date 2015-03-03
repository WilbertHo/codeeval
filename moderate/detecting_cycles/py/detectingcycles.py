#!/usr/bin/env python
"""
Given a sequence, write a program to detect cycles within it.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename containing a sequence of numbers (space delimited). The file can have multiple such lines. E.g

1
2
3
2 0 6 3 1 6 3 1 6 3 1
3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49
1 2 3 1 2 3 1 2 3

OUTPUT SAMPLE:

Print to stdout the first cycle you find in each sequence. Ensure that there are no trailing empty spaces on each line you print. E.g.

1
2
3
6 3 1
49
1 2 3

The cycle detection problem is explained more widely on wiki

Constraints:
The elements of the sequence are integers in range [0, 99]
The length of the sequence is in range [0, 50]
"""
import fileinput
import re


def detect_cycle(s):
    """ Return the first, longest repeated sequence in s.
        @params:
            s: list
        @returns:
            list

        Iterate through sequence s, storing the position of each
        element in a dict. If an element is already in the dict,
        a repeat has been found. Iterate forward from the found
        index until a mismatch or until the found index iterator
        reaches the current index.
        '20631' -> {2:0, 0:1, 6:2, 3:3, 1:4}
        '206316' -> 6 at index=5 matches 6 at index=2, iterate
                    forward from index 2 a mismatch is found or
                    until index 5.
    """
    found = dict()
    repeated_seq = list()
    for i, c in enumerate(s):
        if c not in found:
            found[c] = i
        else:
            # Iterate over a range starting with the index where the
            # 1st match is found up to the current index, and the
            # current index to the end of the sequence. Doesn't
            # matter if the lengths, don't match, zip will take care
            # of it.
            for original_i, repeated_i in zip(range(found[c], i),
                                              range(i, len(s))):
                if s[original_i] == s[repeated_i]:
                    repeated_seq.append(s[original_i])
                else:
                    break
            break

    # No match found, return the original string
    return repeated_seq or s


def main():
    lines = [line.strip() for line in fileinput.input() if line]

    for line in lines:
        print ' '.join(detect_cycle(re.split(r'\s+', line)))


if __name__ == '__main__':
    main()
