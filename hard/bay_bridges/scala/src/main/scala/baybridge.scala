class Point(val x: Double, val y: Double) {}
class Segment(val head: Point, val tail: Point) {}

class BayBridges {
  def intersection(s1: Segment, s2:Segment): Point = {
    /* Calculate the point of intersection between segments s1 and s2.
     * Extend line segments s1 and 2 to infinity and calculate the
     * point of intersection.
     */ 

      val x = ((s1.head.x * s1.tail.y - s1.head.y * s1.tail.x) * (s2.head.x - s2.tail.x) - (s1.head.x - s1.tail.x) * (s2.head.x * s2.tail.y - s2.head.y * s2.tail.x)) /
              ((s1.head.x - s1.tail.x) * (s2.head.y - s2.tail.y) - (s1.head.y - s1.tail.y) * (s2.head.x - s2.tail.x))

      val y = ((s1.head.x * s1.tail.y - s1.head.y * s1.tail.x) * (s2.head.y - s2.tail.y) - (s1.head.y - s1.tail.y) * (s2.head.x * s2.tail.y - s2.head.y * s2.tail.x)) /
              ((s1.head.x - s1.tail.x) * (s2.head.y - s2.tail.y) - (s1.head.y - s1.tail.y) * (s2.head.x - s2.tail.x))

      return new Point(x, y)
  }

  def is_between(segment: Segment, point: Point): Boolean = {
    /* Determine if point (x, y) lies on line l.
     * Calculates if point (x, y) lies between the points comprising
     * line segment l.
     */

    val cross = (point.y - segment.head.y) * (segment.tail.x - segment.head.x) - (point.x - segment.head.x) * (segment.tail.y - segment.head.y)
    if (math.abs(math.round(cross)) != 0)
        return false

    val dot = (point.x - segment.head.x) * (segment.tail.x - segment.head.x) + (point.y - segment.head.y) * (segment.tail.y - segment.head.y)
    if (dot < 0)
        return false

    val length = (segment.tail.x - segment.head.x) * (segment.tail.x - segment.head.x) + (segment.tail.y - segment.head.y) * (segment.tail.y - segment.head.y)
    if (dot > length)
        return false

    return true
  }

  def intersects(segment_a: Segment, segment_b: Segment): Boolean = {
    /* Check if line segment_a intersects line segment_b
     * Extend segment_a and segment_b to infinity and calculate the
     * point p of intersection, then determine if point p lies between
     * both segment_a and segment_b.
     */
      
    val foo = List(is_between(segment_a, intersection(segment_a, segment_b)),
                   is_between(segment_b, intersection(segment_a, segment_b)))
    return foo.forall(_ == true)
  }
}

object Main {
  def parse_input(input: Traversable[String]): Map[Int, Segment] = {
    // ("1: ([37.788353, -122.387695], [37.829853, -122.294312])", ...
    // split by ":\s*" becomes:
    // (Array("1", "([37.788353, -122.387695], [37.829853, -122.294312])"))
    return input.map(_.split(""":\s*""")).map {
      case Array(bridge, coords) =>
        (bridge.toInt,
         // "([37.788353, -122.387695], [37.829853, -122.294312])"
         // replace "[^0-9-.]" and convert to double:
         // Array(37.788353, -122.387695, 37.829853, -122.294312)
         coords.split(""",\s*""" ).map(
           _.replaceAll("""[^0-9-.]""", "")).map(
             // Take every 2 values and create a Point object
             _.toDouble).sliding(2, 2).map {
               case Array(x, y) => new Point(x, y)
             // Take 2 Point and create a Segment
             }.sliding(2, 2).map {
               case Seq(x, y) => new Segment(x, y)
             // Take the first (and only) element in the iterator
             }.next()
        )
      }.toMap
  }

  def main(args: Array[String]) {
    val input = (if (args.length < 1) io.Source.stdin
                 else io.Source.fromFile(args(0))).getLines().toVector
    
    print(parse_input(input))
  }
}
