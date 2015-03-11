"""
Credits: This challenge has appeared in a google competition before.
Once upon a time in a strange situation, people called a number ugly
if it was divisible by any of the one-digit primes (2, 3, 5 or 7).
Thus, 14 is ugly, but 13 is fine. 39 is ugly, but 121 is not. Note
that 0 is ugly. Also note that negative numbers can also be ugly: -14
and -39 are examples of such numbers.

One day on your free time, you are gazing at a string of digits,
something like:

123456
You are amused by how many possibilities there are if you are allowed
to insert plus or minus signs between the digits. For example you can
make:
1 + 234 - 5 + 6 = 236
which is ugly. Or

123 + 4 - 56 = 71
which is not ugly.

It is easy to count the number of different ways you can play with the
digits: Between each two adjacent digits you may choose put a plus
sign, a minus sign, or nothing. Therefore, if you start with D digits
there are 3^(D-1) expressions you can make. Note that it is fine to
have leading zeros for a number. If the string is '01023', then
'01023', '0+1-02+3' and '01-023' are legal expressions.

Your task is simple: Among the 3^(D-1) expressions, count how many of
them evaluate to an ugly number.

INPUT SAMPLE: Your program should accept as its first argument a path
to a filename. Each line in this file is one test case. Each test case
will be a single line containing a non-empty string of decimal digits.
The string in each test case will be non-empty and will contain only
characters '0' through '9'. Each string is no more than 13 characters
long. E.g.

1
9
011
12345

OUTPUT SAMPLE:
Print out the number of expressions that evaluate to an ugly number
for each test case, each one on a new line. E.g.

0
1
6
64
"""
from collections import deque
import fileinput
from itertools import chain, combinations, islice, permutations, product


def get_all_substrings(string):
    """ Return all substrings of input string combined with '-' and '+'
    """
    OPERATORS = '-+'
    # Generate all the possible places we could split the string
    # Ex, for string 'abcde'
    # 1 split -> a bcde, ab cde, abc de, abcd e
    # 2 splits -> a b cde, a bc de
    # We'll model where to split the string by creating power sets
    # for length starting from 2 until the length of the input string
    # (0, 1), (0, 2), ..., (0, 1, 2), ..., (0, 1, 2, 3, 4)
    # The resulting power sets will have duplicates, ie (1, 3, 4) and
    # (0, 1, 3, 4) so we solve this by removing the 0 and creating a
    # set.
    splits = set(map(lambda x: filter(None, x),
                     chain.from_iterable(combinations(range(len(string)), r)
                                         for r in range(2, len(string) + 1))))

    substrings = [[string], ['-', string]]
    for split in splits:
        # Create a power set of '-, +' of the length of the split, with an
        # additional token for the leading 0 position
        # (1, 2) -> [(-, -, -), (-, -, +), (-, +, -), ...
        signs = map(deque, product(OPERATORS, repeat=len(split)+1))

        # Convert the (1, 2) string split specifiers into slice notation
        # ex (1, 2) for 'abcd' 
        # zip([0, 1, 2, 4], [1, 2, 4]) == [(0, 1), (1, 2), (2, 4)]
        slices = zip(*(islice((0,) + split + (len(string),), n, None)
                       for n in range(2)))
        sliced_string = map(lambda (start, end): string[start:end],
                            slices)

        # Zip up the signs with the sliced up string
        # ex: zip(['-', '+', '-'],
        #         ['a', 'bc', 'cde'])
        substrings.extend(map(lambda sign: list(chain.from_iterable(
                                            zip(sign, sliced_string))),
                              signs))

    return substrings or [string]


def is_ugly(n):
    if n == 0 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return True
    return False


def main():
    lines = [line.strip() for line in fileinput.input()]

    for line in lines:
        substrings = get_all_substrings(line)
        print substrings


if __name__ == '__main__':
    main()
