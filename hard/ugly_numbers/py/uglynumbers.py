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
import fileinput
from itertools import izip, product
from operator import add, sub


def get_all_substrings(string):
    num_ugly = 0
    string_n = map(int, string)[::-1]

    for ops in product([None, True, False], repeat=len(string)-1):
        # Iterate over a pseudo-power set of no-op, add and sub
        # with None being no-op, True being add, False being sub
        # The reason for this is True/False comparisons are fast(er)
        # [(, , ), (, ,+), (,,-),
        #  (,+,+), (,-,-)
        # So we can combine the string and one of the op tuples, ex:
        # 1234, ( , , ) -> 1234
        # 1234, ( ,+,+) -> 12+3+4
        # 1234, ( ,+,-) -> 12+3-4
        accum = 0
        mod = 0
        for digit, op in izip(string_n, reversed((None,) + ops)):
            if op is None:
                accum += digit * 10 ** mod
                mod += 1
            elif op:
                accum += digit * 10 ** mod
                mod = 0
            else:
                accum = -1 * (accum + digit * 10 ** mod)
                mod = 0
        # Check if the accum is ugly, so we don't have to iterate again
        # Save some time, again, by not calling a function
        if accum == 0:
            num_ugly +=1
            continue
        if accum % 2 == 0:
            num_ugly +=1
            continue
        if accum % 3 == 0:
            num_ugly +=1
            continue
        if accum % 5 == 0:
            num_ugly +=1
            continue
        if accum % 7 == 0:
            num_ugly +=1
            continue

    return num_ugly


def main():
    lines = [line.strip() for line in fileinput.input() if line]

    for line in lines:
        print get_all_substrings(line)


if __name__ == '__main__':
    main()
