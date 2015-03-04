#!/usr/bin/env python
"""
Given a list of numbers and a positive integer k, reverse the elements of the list, k items at a time. If the number of elements is not a multiple of k, then the remaining items in the end should be left as is.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains a list of numbers and the number k, separated by a semicolon. The list of numbers are comma delimited. E.g.

1,2,3,4,5;2
1,2,3,4,5;3

OUTPUT SAMPLE:

Print out the new comma separated list of numbers obtained after reversing. E.g.

2,1,4,3,5
3,2,1,4,5
"""
import fileinput
from itertools import chain, islice


def reverse_groups(ar, k):
    """ Reverse the first multiple-of-k elements of ar, k elements at a time.

        Use islice to generate the groups to reverse. islice takes the
        start element and skips the spec'ed number of elements for
        each call. islice(ar, start, stop=None, skip)
        ex:
        list(islice([1,2,3,4,5], 0, None, 2)) -> [1, 3, 5]
        list(islice([1,2,3,4,5], 1, None, 2)) -> [2, 4]
        zipping those two results in [(1,2), (3,4)]
        ex:
        list(islice([1,2,3,4,5], 0, None, 3)) -> [1, 4]
        list(islice([1,2,3,4,5], 1, None, 3)) -> [2, 5]
        list(islice([1,2,3,4,5], 2, None, 3)) -> [3]
        zip([1,4], [2, 5], [3]) -> [(1, 2, 3)]

        Then take the len(ar) % k and add those elements onto the
        result list.
    """
    _reversed = list(chain.from_iterable(
                    map(lambda x: x[::-1],
                        zip(*(islice(ar, i, None, k) for i in range(k))))))

    return _reversed + ar[len(_reversed):]


def main():
    lines = [line.strip() for line in fileinput.input() if line]

    for line in lines:
        ar, k = line.split(';')
        print ','.join(reverse_groups(ar.split(','), int(k)))


if __name__ == '__main__':
    main()
