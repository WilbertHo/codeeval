#!/usr/bin/env python
from collections import defaultdict
import fileinput


def longest_lines(n, input):
    lengths = dict([(len(i), i) for i in input])
    return [lengths.get(i) for i in list(reversed(sorted(lengths)))[:n]]


def main():
    input = [line.strip('\n') for line in fileinput.input()]
    print '\n'.join(longest_lines(int(input[0]), input[1:]))

if __name__ == '__main__':
    main()
