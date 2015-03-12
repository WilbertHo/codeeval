object Main {
  def product[A](string:Traversable[A], repeat:Int = 1): Vector[Vector[A]] = {
    if (repeat == 1) string.map(Vector(_)).toVector
    else {
      product(string, repeat - 1).flatMap(a => string.map(a ++ Vector(_))).toVector
    }
  }

  def get_all_substrings(string:String): IndexedSeq[Vector[Int]] = {
    /**
     * Return the set of all substrings for a given string.
     *
     * For a string with length n, we'll need 1 to n - 1 spaces, in
     * 1 to n - 1 positions along the string.
     * Ex: for "1234" (n == 4), we can split in 1, 2 and/or 3 places
     * and we can place those splits at index 1, 2 and/or 3.
     * 1 split: 1 234, 12 34, 123 4
     * 2 splits: 1 2 34, 12 3 4, 1 23 4
     * 3 splits (n - 1): 1 2 3 4
     */
    val OPERATORS = Map('+' -> ((a:Int) => a),
                        '-' -> ((a:Int) => -1 * a))
    val slices = (1 until string.length).flatMap(
                  (1 until string.length).combinations(_)).map(
                    Vector(0) ++ _ ++ Vector(string.length)).map(
                      _.sliding(2).toVector)
    val sliced_string = slices.map(slice =>
          slice.map {
            case Vector(start, end) => string.slice(start, end).toInt
          })
    return sliced_string.flatMap { sliced =>
      val operations = product(OPERATORS.values, sliced.length - 1).map(
        Vector(OPERATORS('+')) ++ _)
      operations.map { operation =>
        operation.zip(sliced).map {
          case (func, arg) => func(arg)
        }
      }
    }
  }

  def main(args: Array[String]) {
    val inputs = (if (args.length < 1) io.Source.stdin
                 else io.Source.fromFile(args(0))).getLines().toVector

    println(inputs.map(get_all_substrings(_).map(_.reduce(_ + _))))
  }
}
