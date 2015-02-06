#!/usr/bin/env python
import fileinput
import re
from ctypes import Structure, c_double
from itertools import combinations


class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]

# class Segment(Structure):
#     _fields_ = [('head', Point), ('tail', Point)]

class Segment(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    # formulas are from
    # https://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment
    def has_point(self, point):
        """ Determine if point (x, y) lies on this line. 
            Calculates if point (x, y) lies between the points comprising
            this line segment.
            params:
                point: Point
        """
        cross = (point.y - self.head.y) * (self.tail.x - self.head.x) - (point.x - self.head.x) * (self.tail.y - self.head.y)
        if abs(round(cross)) != 0:
            return False

        dot = (point.x - self.head.x) * (self.tail.x - self.head.x) + (point.y - self.head.y) * (self.tail.y - self.head.y)
        if dot < 0:
            return False

        length = (self.tail.x - self.head.x) * (self.tail.x - self.head.x) + (self.tail.y - self.head.y) * (self.tail.y - self.head.y)
        if dot > length:
            return False

        return True

    # intersection formulas are from
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
    def intersection(self, s):
        """ Calculate the point of intersection between self and segment s.
            Extend self and segment s to infinity and calculate the
            point of intersection.
            params:
                s: Segment
        """
        x = ((self.head.x * self.tail.y - self.head.y * self.tail.x) * (s.head.x - s.tail.x) - (self.head.x - self.tail.x) * (s.head.x * s.tail.y - s.head.y * s.tail.x)) / \
            ((self.head.x - self.tail.x) * (s.head.y - s.tail.y) - (self.head.y - self.tail.y) * (s.head.x - s.tail.x))

        y = ((self.head.x * self.tail.y - self.head.y * self.tail.x) * (s.head.y - s.tail.y) - (self.head.y - self.tail.y) * (s.head.x * s.tail.y - s.head.y * s.tail.x)) / \
            ((self.head.x - self.tail.x) * (s.head.y - s.tail.y) - (self.head.y - self.tail.y) * (s.head.x - s.tail.x))

        return Point(x, y)

    def intersects(self, s):
        """ Check if self intersects segment s
            Extend self and segment s to infinity and calculate the
            point p of intersection, then determine if point p lies between
            both self and segment s.
            params:
                s: Segment
        """
        return self.has_point(self.intersection(s)) and \
               s.has_point(s.intersection(self))


def get_nonintersecting(bridges):
    """ Return largest set of non-intersecting bridges
        Finds all combinations of bridges and calculates if there
        are any intersections.
        ex Check [1, 2, 3, 4, 5, 6], then [1, 2, 3, 4, 5], then
           [1, 2, 3, 4, 6], ..., [1], [2], [3]
        params:
            bridges: dict, map of bridge number to segment
        returns:
            non-intersecting bridges (list of ints)
    """
    crossing_bridges = [[bridge_a, bridge_b]
                        for (bridge_a, segment_a), (bridge_b, segment_b)
                        in combinations(bridges.iteritems(), 2)
                        if segment_a.intersects(segment_b)]

    # crossing_bridges is a nested list of crossing bridges, so we
    # need to flatten it. ex: [[a, b], [a, c]] -> [a, b, a, c]
    crossing_bridges = set([bridge for _bridges in crossing_bridges
                            for bridge in _bridges])

    # Start testing a subset of bridges without one or more of the
    # bridges known to intersect
    for size in range(1, len(crossing_bridges) + 1):
        for intersecting in combinations(crossing_bridges, size):
            subset = dict([(k, v) for k, v in bridges.iteritems() if k not in intersecting])
            if (all([not segment_a.intersects(segment_b)
                     for (bridge_a, segment_a), (bridge_b, segment_b)
                     in combinations(subset.iteritems(), 2)])):
                return map(int, subset)


def main():
    def parse_input(input):
        def str_to_coord(x):
            return float(re.sub(r'[^0-9-.]', '', x))

        bridge_number, coords = re.split(':\s*', input)
        bridge_number = int(bridge_number)
        x1, y1, x2, y2 = map(str_to_coord, re.split(',\s*', coords))
        return (bridge_number, Segment(Point(x1, y1), Point(x2, y2)))

    input = [line.strip() for line in fileinput.input()]
    bridges = dict(map(parse_input, input))

    print '\n'.join(map(lambda x: str(x), get_nonintersecting(bridges)))


if __name__ == '__main__':
    main()
