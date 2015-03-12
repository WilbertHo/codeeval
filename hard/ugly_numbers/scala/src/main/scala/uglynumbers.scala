object Main {
  def product(string:String, repeat:Int = 1): Traversable[Traversable[Char]] = {
    if (repeat == 1) string.map(Vector(_))
    else {
      product(string, repeat - 1).flatMap(a => string.map(a ++ Vector(_)))
    }
  }

  def get_all_substrings(string:String) {
    // For a string with length 4, ex: '1234', find all possible places
    // where we can split in 1, 2 or 3 places:
    // 1 234, 12 34, 123 4
    // 1 2 34, 12 3 4, 1 23 4
    // 1 2 3 4
    val slices = (1 until string.length).flatMap(
                  (1 until string.length).combinations(_)).map(
                    Vector(0) ++ _ ++ Vector(string.length))
    slices.foreach { println }
  }

  def main(args: Array[String]) {
    val inputs = (if (args.length < 1) io.Source.stdin
                 else io.Source.fromFile(args(0))).getLines().toVector

    for (input <- inputs) get_all_substrings(input)
  }
}
