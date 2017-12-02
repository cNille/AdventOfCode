val result = 
  scala.io.Source.fromFile("my.input").getLines.toList
  .map(
    _.split(" ")
      .filter(_.length > 0)
      .map(_.toInt)
      .sorted
  )
  .map(x => x.last - x.head )
  .sum
println(result)
