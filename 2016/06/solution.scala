// Part 1 && Part 2
val result = scala.io.Source.fromFile("data.txt")
  .getLines.toList                                          // List[String]
  .flatMap(x => x.zipWithIndex.map{ case (c,i) => i -> c }) // List[(Int, Char)] - all chars and their position in string
  .groupBy(_._1).mapValues(_.map(_._2))                     // Map[Int -> List[Char]] - all positions with their characters
  .toSeq.sortWith((a,b) => a._1 < b._1)                     // List[Int -> List[Char]] - sort after positions
  .map((x) => 
    (x._1, x._2.groupBy(identity)                           // Groups all characters within a position
    .mapValues(_.size).toList                               // Get occurrences number from the grouped list
    .sortWith((a,b)=>a._2<b._2)(0))                         // Sort after least occurences. Res on part 2
//  .sortWith((a,b)=>a._2>b._2)(0))                         // Sort after most  occurences. Res on part 1
  )
  .map(_._2._1).mkString                                    // Makes a string of the list withthe most/least common characters
println(s"Result: $result")
