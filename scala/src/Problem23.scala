import scala.annotation.tailrec

/*
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the
proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
*/

// super slow, not really working haha, first scala in a long time :)
object Problem23 {
  val MAX_NUM = 28123
  val SMALLEST_ABUNDANT = 12

  def main(args: Array[String]): Unit = {
    println("Hello, world!")

    println(Stream.range(1, MAX_NUM).filter(hasAbundablePair).sum)
  }

  def hasAbundablePair(num: Int): Boolean = {
    if (num > MAX_NUM) true
    else if (num < 24) false
    else {
      for (abundable <- abundantStream().takeWhile((p) => p <= num / 2);
           abundablep <- abundantStream().dropWhile((p) => p < abundable).takeWhile((p) => abundable + p <= num)
           if abundable + abundablep == num) {
        return true
      }
      false
    }
  }

  def abundantStream(): Stream[Int] = abundanceTestStream().filter((p) => p._2).map((p) => p._1)

  def abundanceTestStream(): Stream[(Int, Boolean)] = sumsProperDivisorsStream.zipWithIndex.map((p) => (p._2, p._2 < p._1))

  def sumsProperDivisorsStream(): Stream[Int] = properDivisorsStream().map((xs) => xs.sum)

  def properDivisorsStream(): Stream[Seq[Int]] = Stream.from(0) map properDivisors

  def properDivisors(num: Int): Seq[Int] = {
    lazy val biggest_candidate = math.sqrt(num)

    @tailrec
    def _properDivisors(div: Int, divisors: Seq[Int]): Seq[Int] = div match {
      case _ if div > biggest_candidate => divisors
      case div if num % div == 0 => if ((num / div) == div) _properDivisors(div + 1, divisors :+ div)
      else _properDivisors(div + 1, divisors :+ div :+ num / div)
      case div => _properDivisors(div + 1, divisors)
    }

    num match {
      case 0 => Nil
      case _ => _properDivisors(2, Seq(1))
    }
  }

}
