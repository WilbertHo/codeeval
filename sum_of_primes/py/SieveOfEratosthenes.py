#!/usr/bin/env python


def sieve_of_eratosthenes(n):
    # Generate a list of possible primes, with 1 denoting prime and 0
    # denoting not-prime
    nums = [1 for i in xrange(0, n + 1)]

    # Start at the first prime number, p = 2, and set all multiples
    # of p to not-prime
    # Find the next number greater than p that hasn't been marked
    # not-prime and repeat
    for i in xrange(2, n + 1):
        if nums[i] == 0:
            continue
        # for j in xrange(i << 1, n + 1, i):
        for j in xrange(i * 2, n + 1, i):
            nums[j] = 0

    # 0 and 1 are not prime numbers, return any marked as prime
    return [i for i in xrange(0, len(nums)) if nums[i] == 1][2:]


if __name__ == '__main__':
    pass
