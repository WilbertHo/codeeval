#!/usr/bin/env python
import fileinput
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


def main():
    lines = [line.strip() for line in fileinput.input()]

    for line in lines:
        fizz, buzz, n = map(int, line.split())
        output = map(lambda n: fizzbuzz(fizz, buzz, n), range(1, n + 1))
        print " ".join(output)


if __name__ == '__main__':
    main()
