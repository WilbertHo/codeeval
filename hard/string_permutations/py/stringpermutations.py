#!/usr/bin/env python

# Write a program which prints all the permutations of a string in
# alphabetical order.
# We consider that digits < upper case letters < lower case letters.
# The sorting should be performed in ascending order.

import fileinput


def permutations(ar):
    if len(ar) == 1:
        return ar
    accum = list()
    # 'abc' -> 'a' + 'bc'
    #          'bc' -> ['bc', 'cb']
    #          ['a' + perm for perm in ['bc', 'cb']] -> ['abc', 'acb']
    #       -> 'b' + 'ac'
    #          'ac' -> ['ac', 'ca']
    #          ['b' + perm for perm in ['ac', 'ca']] -> ['bac', 'bca']
    for i, c in enumerate(ar):
        accum.extend([c + perm for perm in permutations(ar[:i] + ar[i+1:])])
    return accum


def main():
    # print permutations('bc')
    print permutations('abc')


if __name__ == '__main__':
    main()
