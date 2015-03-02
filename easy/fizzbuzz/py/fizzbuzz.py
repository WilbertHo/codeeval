#!/usr/bin/env python
import fileinput
import functools
import multiprocessing
import sys


def fizzbuzz(fizz, buzz, n):
    token = ''
    if n % fizz == 0:
        token += 'F'
    if n % buzz == 0:
        token += 'B'
    if not token:
        token = str(n)
    return token


def fizzbuzz_helper(_args):
    fizz, buzz, n = map(int, _args.split())
    return map(functools.partial(fizzbuzz, fizz, buzz), range(1, n + 1))


def main():
    lines = [line.strip() for line in fileinput.input() if line]

    pool = multiprocessing.Pool()
    output = pool.map(fizzbuzz_helper, lines)

    for line in output:
        print " ".join(line)


if __name__ == '__main__':
    main()
