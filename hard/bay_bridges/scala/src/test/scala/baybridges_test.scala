import org.scalatest._

class BayBridgesSpecs extends FlatSpec with Matchers {
  it should "segment has_point" in {
    val head = new Point(37.788353, -122.387695)
    val tail = new Point(37.829853, -122.294312)
    val not_in_between = new Point(37.474858, -122.131577)
    val segment = new Segment(head, tail)

    segment.has_point(head) should equal (true)
    segment.has_point(not_in_between) should equal (false)
  }

  it should "segment intersects" in {
    val s1 = new Segment(new Point(37.532599, -122.218094),
                         new Point(37.615863, -122.097244))
    val s2 = new Segment(new Point(37.516262, -122.198181),
                         new Point(37.653383, -122.151489))

    val s3 = new Segment(new Point(37.788353, -122.387695),
                         new Point(37.829853, -122.294312))

    val s4 = new Segment(new Point(37.504824, -122.181702),
                         new Point(37.633266,-122.121964))

    s1.intersects(s2) should equal (true)
    s2.intersects(s1) should equal (true)
    s3.intersects(s4) should equal (false)
    s4.intersects(s3) should equal (false)
  }
}
