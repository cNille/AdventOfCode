/*
//Part 1 
val data = scala.io.Source.fromFile("data.txt").mkString
val triReg = """\s*(\d+)\s+(\d+)\s+(\d+)\s*""".r
def triangleIterator (line: String): Boolean = {
  val s = line match { case triReg(s1, s2, s3) => List(s1.toInt, s2.toInt, s3.toInt) }
  return s(0) < s(1) + s(2) && s(1) < s(0) + s(2) && s(2) < s(1) + s(0)
}
val lines = data.split("\n").toList
val nbr = lines.map(triangleIterator).filter { x => x }.length
println(s"Nbr: $nbr")
*/
//Part 2 
val data = scala.io.Source.fromFile("data.txt").mkString
val triReg = """\s*(\d+)\s+(\d+)\s+(\d+)\s*(\d+)\s+(\d+)\s+(\d+)\s*(\d+)\s+(\d+)\s+(\d+)""".r
def triangleIterator (line: String): Int = {
  val triangles: List[List[Int]] = line match { 
    case triReg(a1, b1, c1, a2, b2, c2, a3, b3, c3) => 
      List( List(a1.toInt, a2.toInt, a3.toInt), List(b1.toInt, b2.toInt, b3.toInt),
        List(c1.toInt, c2.toInt, c3.toInt) )
  }
  val possible = triangles.map { s =>  
    if(s(0) < s(1) + s(2) && s(1) < s(0) + s(2) && s(2) < s(1) + s(0)) { 1 } else { 0 }
  }
  return possible.filter( x => x == 1).length 
}
def linesMerger(lines: List[String]): List[String] = {
  val line = List(lines.head, lines.tail.head, lines.tail.tail.head).mkString
  val tail = lines.tail.tail.tail
  return line :: (if(lines.length <= 3) { List() } else { linesMerger(tail) })
}
val lines = data.split("\n").toList
val nbr = linesMerger(lines).map(triangleIterator).sum
println(s"Nbr: $nbr")
