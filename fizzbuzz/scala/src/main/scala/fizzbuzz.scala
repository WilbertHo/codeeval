object FizzBuzz {
  def fizzbuzz(fizz: Int, buzz: Int, end: Int): String = {
    (1 to end).view.map { i =>
      (i % fizz, i % buzz) match {
        case (0, 0) => "FB"
        case (0, _) => "F"
        case (_, 0) => "B"
        case _ => i
      }
    } mkString(" ")
  }

  def main(args: Array[String]) {
    val input = (if (args.length < 1) io.Source.stdin
                 else io.Source.fromFile(args(0)))

    for (line <- input.getLines.map(_.split(' ')).toVector) {
      val Array(fizz, buzz, end) = line.map(_.toInt)
      println(fizzbuzz(fizz, buzz, end))
    }
  }
}
