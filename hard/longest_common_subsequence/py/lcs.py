#!/usr/bin/env python
import fileinput


def longest_common_subsequence(s1, s2):
    """ Return the longest common subsequence of two strings, s1 and s2.
        params:
            string: s1
            string: s2
        returns:
            longest common subsequence: string
    """
    # Create a 2D array to keep track of the LCS between two
    # substrings of s2, s2
    lcs = list()
    for i in enumerate(s1, start=1):
        row = list()
        for j in enumerate(s2, start=2):
            pass


def main():
    input = [line.strip() for line in fileinput.input()].pop().split(';')
    print longest_common_subsequence(*input)


if __name__ == '__main__':
    main()
