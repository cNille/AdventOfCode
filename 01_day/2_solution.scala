val nums = scala.io.Source
  .fromFile("my.input")
  .getLines
  .toList
  .head
  .toList
  .map(_.toInt - 48)

val halfs = nums.splitAt(nums.length / 2)

val tuples = halfs._1 zip halfs._2
println(tuples)
val result = tuples
  .filter(x => x._1 == x._2)
  .map( x => x._1 + + x._1)
  .reduce(_ + _)

println(result)
