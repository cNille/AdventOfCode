import math.{sin, abs, cos}
val lines = scala.io.Source.fromFile("data.txt").mkString
val instructions = lines.split(", ").toList
def instructionIterator(instructions: List[String], orientation: Int) : List[(Int, Int)] = {
  if(instructions.length <= 0){
    return List()
  }
  val i = instructions.head
  val newOrientation: Int = if(i.head == 'R'){ orientation - 90 } else { 
    orientation + 90 } 
  val length = i.tail.trim.toInt
  val dx = length * cos(newOrientation * (scala.math.Pi / 180)).toInt
  val dy = length * sin(newOrientation * (scala.math.Pi / 180)).toInt
  return List((dx, dy)) ::: instructionIterator(instructions.tail, newOrientation)
}
val list = instructionIterator(instructions, 90)
val sum = list.reduce[(Int, Int)] { (acc, n) => (acc._1 + n._1, acc._2 + n._2)}
val shortestPath = abs(sum._1) + abs(sum._2)
println(s"Shortest Path is: $shortestPath")

// Part 2:
def op(acc: List[(Int,Int)], x: (Int,Int)): List[(Int,Int)] = {
  val nx = if(x._1 < 0) { -1 } else { 1 }
  val ny = if(x._2 < 0) { -1 } else { 1 }
  val dx = List.range(1, abs(x._1) + 1).map(i => (i * nx + acc.head._1, acc.head._2)).reverse
  val dy = List.range(1, abs(x._2) + 1).map(i => (acc.head._1, i * ny + acc.head._2)).reverse
  dx ::: dy ::: acc
}
val locations = list.foldLeft(List((0,0)))(op).reverse
val dup = locations.groupBy(identity).filter(_._2.size > 1).map(_._1)
val filtered = locations.filter(x => dup.contains(x._1) && dup(x._1) == x._2 )
if(filtered.length > 0){
  val first = filtered.head
  val dist = abs(first._1) + abs(first._2)
  println(s"Distance: $dist")
} else {
  println("No duplicate found")
}
