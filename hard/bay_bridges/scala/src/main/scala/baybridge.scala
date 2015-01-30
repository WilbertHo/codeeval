class BayBridges {
}

object Main {
  def parse_input(input: Traversable[String]): Map[Int,Array[Double]] = {
    return input.map(_.split(""":\s*""")).map(x=>(x(0).toInt, x(1).split(""",\s*""").map(_.replaceAll("""[^0-9-.]""", "")).map(_.toDouble))).toMap
  }

  def main(args: Array[String]) {
    val input = (if (args.length < 1) io.Source.stdin
                 else io.Source.fromFile(args(0))).getLines().toVector
    
    parse_input(input)
  }
}
