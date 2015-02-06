import org.scalatest._

class BayBridgesSpecs extends FlatSpec with Matchers {
  it should "is between" in {
    val bb = new BayBridges()

    val head = new Point(37.788353, -122.387695)
    val tail = new Point(37.829853, -122.294312)
    val not_in_between = new Point(37.474858, -122.131577)
    val segment = new Segment(head, tail)

    bb.is_between(segment, head) should equal (true)
    bb.is_between(segment, not_in_between) should equal (false)
  }

  it should "intersects" in {
    val bb = new BayBridges()

    val s1 = new Segment(new Point(37.532599, -122.218094),
                         new Point(37.615863, -122.097244))
    val s2 = new Segment(new Point(37.516262, -122.198181),
                         new Point(37.653383, -122.151489))

    val s3 = new Segment(new Point(37.788353, -122.387695),
                         new Point(37.829853, -122.294312))

    val s4 = new Segment(new Point(37.504824, -122.181702),
                         new Point(37.633266,-122.121964))

    bb.intersects(s1, s2) should equal (true)
    bb.intersects(s3, s4) should equal (false)
  }
}
