#!/usr/bin/env python

import fileinput


class Stack(object):
    def __init__(self, input=None):
        self.stack = [int(i) for i in input] if input else []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return False if self.stack else True


def main():
    input = [line.strip() for line in fileinput.input()]

    for line in input:
        stack = Stack()
        for i, elem in enumerate(line.split()):
            stack.push(int(elem))

        while not stack.empty():
            print stack.pop(),
            if not stack.empty():
                stack.pop()
        print ''


if __name__ == '__main__':
    main()
