#!/usr/bin/env python
import fileinput
import re
from collections import namedtuple
from decimal import Decimal, getcontext
from itertools import combinations


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
def is_between(segment, coord):
    """ Determine if coordinate (x, y) lies on line l.
        Calculates if coord (x, y) lies between the coords comprising
        line segment l.
        params:
            line: Segment
            coord: Coord
    """
    cross = (coord.y - segment.head.y) * (segment.tail.x - segment.head.x) - (coord.x - segment.head.x) * (segment.tail.y - segment.head.y)
    if abs(cross.quantize(Decimal('.000001'))) != 0:
        return False

    dot = (coord.x - segment.head.x) * (segment.tail.x - segment.head.x) + (coord.y - segment.head.y) * (segment.tail.y - segment.head.y)
    if dot < 0:
        return False

    length = (segment.tail.x - segment.head.x) * (segment.tail.x - segment.head.x) + (segment.tail.y - segment.head.y) * (segment.tail.y - segment.head.y)
    if dot > length:
        return False

    return True


# intersection formulas are from
# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
def intersection(s1, s2):
    """ Calculate the point of intersection between segments s1 and s2.
        Extend line segments s1 and 2 to infinity and calculate the
        point of intersection.
        params:
            s1: Segment
            s2: Segment
    """
    x = ((s1.head.x * s1.tail.y - s1.head.y * s1.tail.x) * (s2.head.x - s2.tail.x) - (s1.head.x - s1.tail.x) * (s2.head.x * s2.tail.y - s2.head.y * s2.tail.x)) / \
        ((s1.head.x - s1.tail.x) * (s2.head.y - s2.tail.y) - (s1.head.y - s1.tail.y) * (s2.head.x - s2.tail.x))

    y = ((s1.head.x * s1.tail.y - s1.head.y * s1.tail.x) * (s2.head.y - s2.tail.y) - (s1.head.y - s1.tail.y) * (s2.head.x * s2.tail.y - s2.head.y * s2.tail.x)) / \
        ((s1.head.x - s1.tail.x) * (s2.head.y - s2.tail.y) - (s1.head.y - s1.tail.y) * (s2.head.x - s2.tail.x))

    return x, y


def intersects(segment_a, segment_b):
    """ Check if line segment_a intersects line segment_b
        Extend segment_a and segment_b to infinity and calculate thed
        point p of intersection, then determine if point p lies between
        both segment_a and segment_b.
        params:
            segment_a: Segment
            segment_b: Segment
    """
    return all([is_between(segment_a, Coord(*intersection(segment_a, segment_b))),
                is_between(segment_b, Coord(*intersection(segment_a, segment_b)))])


def non_intersects(bridges):
    """ Return largest set of non-intersecting bridges
        Finds all combinations of bridges and calculates if there
        are any intersections.
        ex Check [1, 2, 3, 4, 5, 6], then [1, 2, 3, 4, 5], then
           [1, 2, 3, 4, 6], ..., [1], [2], [3]
        params:
            bridges:
    """
    for size in range(len(bridges), 0, -1):
        for subset in combinations(bridges.iteritems(), size):
            if (all([not intersects(segment_a, segment_b)
                     for (bridge_a, segment_a), (bridge_b, segment_b)
                     in combinations(subset, 2)])):
                return (map(lambda (bridge, segment): str(int(bridge)),
                            subset))


def main():
    input = [line.strip() for line in fileinput.input()]
    bridges = dict(map(parse_input, input))

    print '\n'.join(non_intersects(bridges))


if __name__ == '__main__':
    main()
