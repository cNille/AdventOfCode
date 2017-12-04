val result = scala.io.Source.fromFile("my.input").getLines.toList
  .map(  
    _.split(' ')
      .map(x => (x,x))
      .groupBy(_._1)
      .values
      .map(_.length)
      .filter(_ > 1)
      .toList 
    ).toList
      .filter(_.length == 0)
      .length

println(result)
