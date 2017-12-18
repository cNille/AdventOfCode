val nums = scala.io.Source
  .fromFile("my.input")
  .getLines
  .toList
  .head
  .toList
  .map(_.toInt - 48)

val nums_2 = (nums.last :: nums).dropRight(1)
val tuples = nums_2 zip nums
val result = tuples
  .filter(x => x._1 == x._2)
  .map(_._1)
  .reduce(_ + _)

println(result)
