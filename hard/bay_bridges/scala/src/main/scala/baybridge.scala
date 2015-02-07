class Point(val x: Double, val y: Double) {}

class Segment(val head: Point, val tail: Point) {
  def intersection(s: Segment): Point = {
    /* Calculate the point of intersection between this and segment s
     * Extend line segments s1 and 2 to infinity and calculate the
     * point of intersection.
     */ 

      val x = ((head.x * tail.y - head.y * tail.x) * (s.head.x - s.tail.x) - (head.x - tail.x) * (s.head.x * s.tail.y - s.head.y * s.tail.x)) /
              ((head.x - tail.x) * (s.head.y - s.tail.y) - (head.y - tail.y) * (s.head.x - s.tail.x))

      val y = ((head.x * tail.y - head.y * tail.x) * (s.head.y - s.tail.y) - (head.y - tail.y) * (s.head.x * s.tail.y - s.head.y * s.tail.x)) /
              ((head.x - tail.x) * (s.head.y - s.tail.y) - (head.y - tail.y) * (s.head.x - s.tail.x))

      return new Point(x, y)
  }

  def intersects(segment: Segment): Boolean = {
    /* Check if line segment_a intersects line segment_b
     * Extend segment_a and segment_b to infinity and calculate the
     * point p of intersection, then determine if point p lies between
     * both segment_a and segment_b.
     */
      
    return has_point(intersection(segment)) &&
           segment.has_point(segment.intersection(this))
  }

  def has_point(point: Point): Boolean = {
    /* Determine if point (x, y) lies on line l.
     * Calculates if point (x, y) lies between the points comprising
     * line segment l.
     */

    val cross = (point.y - head.y) * (tail.x - head.x) - (point.x - head.x) * (tail.y - head.y)
    if (math.abs(math.round(cross)) != 0)
        return false

    val dot = (point.x - head.x) * (tail.x - head.x) + (point.y - head.y) * (tail.y - head.y)
    if (dot < 0)
        return false

    val length = (tail.x - head.x) * (tail.x - head.x) + (tail.y - head.y) * (tail.y - head.y)
    if (dot > length)
        return false

    return true
  }
}

class BayBridges {
  def get_non_intersecting(bridges: Map[Int, Segment]): Seq[Int] = {
    val crossing_bridges = bridges.toSeq.combinations(2).toSeq.flatMap {
      case Seq((bridge_a, segment_a), (bridge_b, segment_b)) =>
        if (segment_a.intersects(segment_b)) {
          Seq(bridge_a, bridge_b)
        } else {
          None
        }
    }.toSet

    for (length <- 1 to crossing_bridges.size) {
      for (subset <- crossing_bridges.toSeq.combinations(length)) {
          if ((bridges.keys.toList.diff(subset).combinations(2).map {
            case Seq(bridge_a, bridge_b) =>
              bridges(bridge_a).intersects(bridges(bridge_b))
          }).forall( _ == false )) {
            return bridges.keys.toList.diff(subset).sorted
          }
      }
    }
  return List(0)
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
    
    val bb = new BayBridges()
    val bridges = parse_input(input)
    println(bb.get_non_intersecting(bridges).mkString("\n"))
  }
}
