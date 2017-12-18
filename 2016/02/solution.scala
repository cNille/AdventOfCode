import scala.math.{abs, min, max}
//Part 1
/*
val data = scala.io.Source.fromFile("data.txt").mkString
def instructionIterator(instructions: String, pos: Int): Int = {
  val dxdy = instructions.head match {
    case 'L' => (-1, 0)
    case 'R' => (1,  0)
    case 'U' => (0, -1)
    case 'D' => (0,  1)
  }
  val newPos = max(1, min(2, ((pos-1) / 3 + dxdy._2)) * 3 + max(1, min(3, ((pos-1)%3 + dxdy._1 + 1))))
  if (instructions.length == 1){ return newPos }
  return instructionIterator(instructions.tail, newPos)
}
val lines = data.split("\n").toList
//println(printer(lines, 5))
def printer(str: List[String], n: Int): String = {
  if(str.length == 0 ){ return "" }
  val x = instructionIterator(str.head, n)
  x.toString + printer(str.tail, x)
}
*/
// Part 2
val data = scala.io.Source.fromFile("data.txt").mkString
def instructionIterator(instructions: String, pos: Int): Int = {
  val row = (pos-1) / 5
  val col = (pos-1) % 5
  val nbrInRow = 5 - 2 * abs(2 - row)
  val nbrInCol = 5 - 2 * abs(2 - col)
  val dxdy = instructions.head match {
    case 'L' => (-1, 0)
    case 'R' => (1,  0)
    case 'U' => (0, -1)
    case 'D' => (0,  1)
  }
  val newX = col + dxdy._1
  val newY = row + dxdy._2
  val xlowerBound = 2 - nbrInRow / 2 + 1 
  val xupperBound = 2 + nbrInRow / 2 + 1
  val ylowerBound = 2 - nbrInCol / 2
  val yupperBound = 2 + nbrInCol / 2
  val newPos = max(1, max( xlowerBound, min(xupperBound, newX + 1)) + max( ylowerBound, min(yupperBound, newY)) * 5)
  if (instructions.length == 1){ return newPos }
  return instructionIterator(instructions.tail, newPos)
}
val lines = data.split("\n").toList
println(converter(lines, 11))
def converter(str: List[String], n: Int): String = {
  if(str.length == 0 ){ return "" }
  val x: Int = instructionIterator(str.head, n)
  val row = ( x - 1) / 5
  val q = if(row > 2) { -1 } else { 1 }
  val newX = Integer.toHexString(x - 6 + (2-row)*(2-row) * q)
  newX.toString + converter(str.tail, x)
}

