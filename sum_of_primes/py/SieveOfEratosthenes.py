#!/usr/bin/env python


class SieveOfEratosthenes(object):
    def __init__(self):
        pass

def sieve_of_eratosthenes(n):
    # generate list of ints from 2 to n
    nums = [1 for i in xrange(0, n + 1)]

    for i in xrange(2, n + 1):
        if nums[i] == 0:
            continue
        j = i
        while(j < n + 1):
            j += i
            if j < len(nums):
                nums[j] = 0

    return [i for i in xrange(0, len(nums)) if nums[i] == 1][2:]


if __name__ == '__main__':
    pass
