from nose.tools import eq_
from baybridges import Point, Segment, intersects, get_nonintersecting


def test_intersects():
    s1 = Segment(Point(37.532599, -122.218094), Point(37.615863, -122.097244))
    s2 = Segment(Point(37.516262, -122.198181), Point(37.653383, -122.151489))
    s3 = Segment(Point(37.788353, -122.387695), Point(37.829853, -122.294312))

    eq_(intersects(s1, s2), True)
    eq_(intersects(s1, s3), False)


def test_get_nonintersecting():
    bridges = {1: Segment(Point(37.532599, -122.218094), Point(37.615863, -122.097244)),
            2: Segment(Point(37.788353, -122.387695), Point(37.829853, -122.294312)),
            3: Segment(Point(37.516262, -122.198181), Point(37.653383, -122.151489))}

    eq_(get_nonintersecting(bridges), [1, 2])
