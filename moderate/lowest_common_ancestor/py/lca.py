#!/usr/bin/env python
import fileinput
import re


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


def build_tree():
    root = Node(30)
    root.left = Node(8)
    root.right = Node(52)

    temp = root.left
    temp.left = Node(3)
    temp.right = Node(20)

    temp = temp.right
    temp.left = Node(10)
    temp.right = Node(29)

    return root


def lca(node, val1, val2):
    if not node:
        return False

    if node.value == val1 or node.value == val2:
        return node.value

    left = lca(node.left, val1, val2)
    right = lca(node.right, val1, val2)

    if left and right:
        return node.value

    return left if left else right


def main():
    lines = [line.strip() for line in fileinput.input() if line]

    bst = build_tree()

    for line in lines:
        print lca(bst, *map(int, re.split(r'\s+', line)))


if __name__ == '__main__':
    main()
