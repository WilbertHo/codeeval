#!/usr/bin/env python

import sys


def main():
    with open(sys.argv[1], 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        try:
            # divisor1 divisor2 numIterations
            div1, div2, iterations = [int(token) for token in line.split()]
        except ValueError:
            # Likely a malformed input line
            print "Shit"

        # Print either the number, F, B, or FB
        for num in range(1, iterations+1):
            if num % div1 == 0 and num % div2 == 0:
                print "FB",
            elif num % div1 == 0:
                print "F",
            elif num % div2 == 0:
                print "B",
            else:
                print num,
        print '\n',

if __name__ == '__main__':
    main()
