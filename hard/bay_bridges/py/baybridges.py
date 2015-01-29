#!/usr/bin/env python
import fileinput
import re
from collections import namedtuple
from decimal import Decimal, getcontext
from itertools import permutations


Coord = namedtuple('Coord', ['x', 'y'])
Segment = namedtuple('Segment', ['head', 'tail'])


def parse_input(input):
    def str_to_coord(x):
        return Decimal(re.sub(r'[^0-9-.]', '', x))

    bridge_number, coords = re.split(':\s*', input)
    bridge_number = str_to_coord(bridge_number)
    x1, y1, x2, y2 = map(str_to_coord, re.split(',\s*', coords))
    return (bridge_number, Segment(Coord(x1, y1), Coord(x2, y2)))


# formulas are from
# https://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment
def is_between(line, coord):
    cross = (coord.y - line.head.y) * (line.tail.x - line.head.x) - (coord.x - line.head.x) * (line.tail.y - line.head.y)
    if abs(cross.quantize(Decimal('.000001'))) != 0:
        return False

    dot = (coord.x - line.head.x) * (line.tail.x - line.head.x) + (coord.y - line.head.y) * (line.tail.y - line.head.y)
    if dot < 0:
        return False

    length = (line.tail.x - line.head.x) * (line.tail.x - line.head.x) + (line.tail.y - line.head.y) * (line.tail.y - line.head.y)
    if dot > length:
        return False

    return True


# intersection formulas are from
# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
def intersection(s1, s2):
    x = ((s1.head.x * s1.tail.y - s1.head.y * s1.tail.x) * (s2.head.x - s2.tail.x) - (s1.head.x - s1.tail.x) * (s2.head.x * s2.tail.y - s2.head.y * s2.tail.x)) / \
        ((s1.head.x - s1.tail.x) * (s2.head.y - s2.tail.y) - (s1.head.y - s1.tail.y) * (s2.head.x - s2.tail.x))

    y = ((s1.head.x * s1.tail.y - s1.head.y * s1.tail.x) * (s2.head.y - s2.tail.y) - (s1.head.y - s1.tail.y) * (s2.head.x * s2.tail.y - s2.head.y * s2.tail.x)) / \
        ((s1.head.x - s1.tail.x) * (s2.head.y - s2.tail.y) - (s1.head.y - s1.tail.y) * (s2.head.x - s2.tail.x))

    return x, y


def intersects(coords_a, coords_b):
    return all([is_between(coords_a, Coord(*intersection(coords_a, coords_b))),
                is_between(coords_b, Coord(*intersection(coords_a, coords_b)))])


def main():
    input = [line.strip() for line in fileinput.input()]
    bridges = dict(map(parse_input, input))

    crossers = set([sorted((bridge_a, bridge_b))[0]
                    for (bridge_a, coords_a), (bridge_b, coords_b)
                    in permutations(bridges.iteritems(), 2)
                    if intersects(coords_a, coords_b)])

    for bridge in sorted(bridges.keys()):
        if bridge not in crossers:
            print bridge


if __name__ == '__main__':
    main()
