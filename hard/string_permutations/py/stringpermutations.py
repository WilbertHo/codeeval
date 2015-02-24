#!/usr/bin/env python

# Write a program which prints all the permutations of a string in
# alphabetical order.
# We consider that digits < upper case letters < lower case letters.
# The sorting should be performed in ascending order.

import fileinput
import re
import string

RATING = dict(zip(list(string.digits + string.uppercase + string.lowercase),
                  range(1, 26 + 26 + 10 + 1)))


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
        # perms = permutations(ar[:i] + ar[i+1:])
        # result = [c + perm for perm in perms]
        # accum.extend(result)
        accum.extend([c + perm for perm in permutations(ar[:i] + ar[i+1:])])
    return accum


def sorter(n):
    """ Sort proxy function
        Return a sort score for n, 0 being the highest
        0: [0]
        000: [0, 0, 0]
        a: [37]
        [[0], [0, 0, 0], [37]]
    """
    score = list()
    for c in n:
        score.append(RATING.get(c))
    return score


def stringpermutations(n):
    return ','.join(sorted(permutations(n), key=sorter))


def main():
    input = [line.strip() for line in fileinput.input()]
    for line in input:
        if not line or re.search(r'[^\d\w]', line):
            continue
        print stringpermutations(line)


if __name__ == '__main__':
    main()
