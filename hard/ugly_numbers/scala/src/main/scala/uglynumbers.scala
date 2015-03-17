object Main {
  def product[A](string:Traversable[A], repeat:Int = 1): Traversable[Vector[A]] = {
    if (repeat == 1) string.map(Vector(_))
    else {
      product(string, repeat - 1).flatMap(a => string.map(a :+ _))
    }
  }

  def get_all_substrings(string:String): Seq[Vector[Long]] = {
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
    val OPERATORS = Map('+' -> ((a:Long) => a),
                        '-' -> ((a:Long) => -1 * a))
    val operations = (1 until string.length).map( n =>
                       (n, product(OPERATORS.values, n).map(
                         OPERATORS('+') +: _))).toMap
    val splits = (1 until string.length).flatMap(
                   (1 until string.length).combinations(_))
    val slices = splits.map(0 +: _ :+ string.length).view.map(
                   _.sliding(2).toVector)
    val sliced_string = slices.map(slice =>
                          slice.map {
                            case Vector(start, end) =>
                              string.slice(start, end).toLong
                          })
    return sliced_string.view.flatMap { sliced =>
      operations(sliced.length - 1).map { operation =>
        operation.zip(sliced).map {
          case (func, arg) => func(arg)
        }
      }
    } :+ Vector(string.toLong)
  }

  def is_ugly(n:Long): Boolean = {
    if (n == 0) return true
    if (n % 2 == 0) return true
    if (n % 3 == 0) return true
    if (n % 5 == 0) return true
    if (n % 7 == 0) return true
    return false
  }

  def main(args: Array[String]) {
    val inputs = (if (args.length < 1) io.Source.stdin
                 else io.Source.fromFile(args(0))).getLines().toVector

    inputs.filter(!_.isEmpty).foreach { input =>
      val substrings = get_all_substrings(input)
      println(substrings.map(_.reduceLeft(_ + _)).map(is_ugly).count(_ == true))
    }
  }
}
