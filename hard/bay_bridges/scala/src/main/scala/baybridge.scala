class Coords(val x: Double, val y: Double) {}
class Segment(val head: Coords, val tail: Coords) {}

class BayBridges {
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
             // Take every 2 values and create a Coords object
             _.toDouble).sliding(2, 2).map {
               case Array(x, y) => new Coords(x, y)
             // Take 2 Coords and create a Segment
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
