#!/usr/bin/env python

import SieveOfEratosthenes

from nose.tools import eq_

def test_sieve_of_eratosthenes():
    eq_(set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        set(SieveOfEratosthenes.sieve_of_eratosthenes(30)))
    eq_(set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]),
        set(SieveOfEratosthenes.sieve_of_eratosthenes(31)))

if __name__ == '__main__':
    pass
