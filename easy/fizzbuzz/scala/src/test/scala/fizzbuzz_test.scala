import org.scalatest._

class FizzBuzzSpecs extends FlatSpec with Matchers {
  it should "3, 5, 10" in {
    val response = FizzBuzz.fizzbuzz(3, 5, 10)
    response should be ("1 2 F 4 B F 7 8 F B")
  }

  it should "2, 7, 15" in {
    val response = FizzBuzz.fizzbuzz(2, 7, 15)
    response should be ("1 F 3 F 5 F B F 9 F 11 F 13 FB 15")
  }
}
