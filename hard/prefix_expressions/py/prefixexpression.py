#!/usr/bin/env python
import fileinput
import operator
import re


def prefix_expression(input):
    # read from right to left
    # if an operator is found, pop 2 operands, push the result
    stack = list()

    operators = { '+': operator.add,
                  '*': operator.mul,
                  '/': operator.truediv }

    for c in input[::-1]:
        if c in operators.keys():
            x = stack.pop()
            y = stack.pop()
            stack.append(operators[c](x, y))
        else:
            stack.append(int(c))

    return int(stack.pop())


def main():
    input = [line.strip() for line in fileinput.input()]

    for line in input:
        print prefix_expression(re.split(r'\s+', line))


if __name__ == '__main__':
    main()
