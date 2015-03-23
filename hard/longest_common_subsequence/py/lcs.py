#!/usr/bin/env python
import fileinput
import re


def longest_common_subsequence_recur(s1, s2):
    """ Return the length of longest common subsequence of two strings.
        C[i][j] = C[i-1][j-1] + 1, if X[i] == Y[j]
                  max(C[i-1][j], C[i][j-1]) if X[i] != Y[j]
        Starting at the end of the strings X and Y, if there is a match,
        we increment the match count, and continue the search with
        the end characters removed, X[:-1], Y[:-1]
        If there isn't a match, then we can safely continue the search
        with X shorter by one symbol, or Y shorter by one symbol.
        params:
            string: s1
            string: s2
        returns:
            longest common subsequence: string
    """
    def lcs_r(s1, s2, s):
        if not s1 or not s2:
            return s
        if s1[-1] == s2[-1]:
            return lcs_r(s1[:-1], s2[:-1], s1[-1] + s)
        else:
            return max([lcs_r(s1[:-1], s2, s), lcs_r(s1, s2[:-1], s)], key=len)

    return lcs_r(s1, s2, '')


def longest_common_subsequence(s1, s2):
    """ Return the longest common subsequence of two strings, s1 and s2.
        C[i][j] = C[i-1][j-1] + 1, if X[i] == Y[j]
                  max(C[i-1][j], C[i][j-1]) if X[i] != Y[j]
        Starting at the end of the strings X and Y, if there is a match,
        we increment the match count, and continue the search with
        the end characters removed, X[:-1], Y[:-1]
        If there isn't a match, then we can safely continue the search
        with X shorter by one symbol, or Y shorter by one symbol.
        params:
            string: s1
            string: s2
        returns:
            longest common subsequence: string
    """
    # Add a space to the beginning of each string so:
    # 1. comparing one string to another of 0-length should be 0
    # 2. makes for easier bounds
    s1 = ' ' + s1
    s2 = ' ' + s2

    # Create a 2D array to keep track of the LCS between two
    # substrings of s1, s2
    length = [[0 for j in range(len(s2))] for i in range(len(s1))]
    lcs = [['' for j in range(len(s2))] for i in range(len(s1))]
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                length[i][j] = length[i - 1][j - 1] + 1
                lcs[i][j] = 'm'
            elif length[i - 1][j] > length[i][j - 1]:
                # Can still find the LCS with s1 shortened by 1
                # ex: s1 = 'AB, s2 = 'B', s1 can drop 'B' and
                # LCS will still be 'A'
                length[i][j] = length[i - 1][j]
                lcs[i][j] = 'i'
            else:
                # Can still find the LCS with s2 shortened by 1
                length[i][j] = length[i][j - 1]
                lcs[i][j] = 'j'

    return print_lcs(lcs, s1, len(s1) - 1, len(s2) - 1)


def print_lcs(lcs, s, i, j, accum=''):
    """ Return the longest common subsequence.
        Iterate over a 2d array starting from the largest i, j values.
        If the element is an 'm', that i (or j) is part of the LCS.
        If the element is an 'i', the array can be shrunk in the i dir.
        If the element is an 'j', the array can be shrunk in the j dir.
        ex:
            _ A C   The first cell to be examined is (3, 2) 'm', so
          _ 0 0 0   'C' is part of the LCS. Continue with [i-1][j-1],
          A 0 m j   meaning we can drop the 'C' from both strings
          B 0 i j   (or just s).
          C 0 i m

            _ A     Examining (2, 1) gives 'i', so we can drop one
          _ 0 0     line in the 'i' direction. This is equivalent
          A 0 m     to comparing 'A' and 'AB' and dropping 'B'
          B 0 i

            _ A     Examining (1, 1) gives 'm', so 'A' is part of
          _ 0 0     the LCS.
          A 0 m     Continue with [i-1][j-1]

            _       i/j are 0, so we're done.
          _ 0
    """
    def print_array():
        for _i in range(i + 1):
            for _j in range(j + 1):
                print (lcs[_i][_j] if lcs[_i][_j] else '0'),
            print ''

    if not i or not j:
        return accum
    if lcs[i][j] == 'm':
        return print_lcs(lcs, s, i - 1, j - 1, s[i] + accum)
    elif lcs[i][j] == 'i':
        return print_lcs(lcs, s, i - 1, j, accum)
    else:
        return print_lcs(lcs, s, i, j - 1, accum)


def main():
    input = [line.strip() for line in fileinput.input()]
    for line in input:
        if not re.search(r';', line):
            continue
        print longest_common_subsequence(*line.split(';'))


if __name__ == '__main__':
    main()
