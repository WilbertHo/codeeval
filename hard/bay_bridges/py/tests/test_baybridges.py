from nose.tools import eq_
from baybridges import Point, Segment, get_nonintersecting


def test_intersects():
    s1 = Segment(Point(37.532599, -122.218094), Point(37.615863, -122.097244))
    s2 = Segment(Point(37.788353, -122.387695), Point(37.829853, -122.294312))
    s3 = Segment(Point(37.516262, -122.198181), Point(37.653383, -122.151489))

    eq_(s1.intersects(s2), False)
    eq_(s2.intersects(s1), False)
    eq_(s1.intersects(s3), True)
    eq_(s3.intersects(s1), True)


def test_has_point():
    point = Point(37.788353, -122.387695)
    s1 = Segment(point, Point(37.829853, -122.294312))
    out = Point(37.474858, -122.131577)

    eq_(s1.has_point(point), True)
    eq_(s1.has_point(out), False)


def test_get_nonintersecting():
    bridges = {1: Segment(Point(37.532599, -122.218094), Point(37.615863, -122.097244)),
            2: Segment(Point(37.788353, -122.387695), Point(37.829853, -122.294312)),
            3: Segment(Point(37.516262, -122.198181), Point(37.653383, -122.151489))}

    eq_(get_nonintersecting(bridges), [2, 3])
