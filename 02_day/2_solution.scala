val result = 
  scala.io.Source.fromFile("my.input")
  .getLines.toList
  .map(
    _.split(" ")
      .filter(_.length > 0)
      .map(_.toInt)
      .combinations(2)
      .toList
      .filter( x => x(0) % x(1) == 0 || x(1) % x(0) == 0 )
      .map(x => scala.math.max(x(0),x(1)) / scala.math.min(x(0),x(1)))
  ).map(_.head).sum
println(result)
