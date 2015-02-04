#!/usr/bin/env python
from collections import defaultdict
import fileinput


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
    def helper(s1, s2, accum, s):
        if not s1 or not s2:
            return accum.update({len(s): s})
        if s1[-1] == s2[-1]:
            return helper(s1[:-1], s2[:-1], accum, s1[-1] + s)
        else:
            return max(helper(s1[:-1], s2, accum, s),
                       helper(s1, s2[:-1], accum, s))

    # if not s1 or not s2:
    #     return 0
    # if s1[-1] == s2[-1]:
    #     return longest_common_subsequence_recur(s1[:-1], s2[:-1]) + 1
    # else:
    #     return max(longest_common_subsequence_recur(s1[:-1], s2),
    #                longest_common_subsequence_recur(s1, s2[:-1]))

    accum = dict()
    helper(s1, s2, accum, '')
    return accum.get(max(accum.keys()))


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
    s1 = ' ' + s1
    s2 = ' ' + s2
    # Create a 2D array to keep track of the LCS between two
    # substrings of s1, s2
    lcs = [[0 for i in range(len(s1))] for j in range(len(s2))]
    for i in enumerate(s1, start=1):
        for j in enumerate(s2, start=1):
            pass


def main():
    input = [line.strip() for line in fileinput.input()].pop().split(';')
    print longest_common_subsequence_recur(*input)


if __name__ == '__main__':
    main()
