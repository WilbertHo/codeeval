#!/usr/bin/env python

import math


def is_palindrome(n):
    if len(n) == 0:
        return False
    if len(n) == 1:
        return True
    if n[0] == n[-1]:
        return is_palindrome(n[1:-1])
    else:
        return False


def is_prime(n):
    for i in range(int(math.sqrt(n)), 1, -1):
        if n % i == 0:
            return False
    return True

def main():
    n = 1000
    while True:
        if is_palindrome(str(n)) and is_prime(n):
            print n
            return
        else:
            n -= 1


if __name__ == '__main__':
    main()
