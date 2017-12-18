val instructions = scala.io.Source.fromFile("data.txt").getLines.toList
// Define display size
val ROW = 6
val COL = 50
// Define regex
val rectReg = """rect (\d+)x(\d+)"""r
val rotColReg = """rotate column x=(\d+) by (\d+)"""r
val rotRowReg = """rotate row y=(\d+) by (\d+)"""r

def rect(x: Int, y: Int, display: List[(Int, Int)]): List[(Int,Int)] = {
  val newLights = (0 until x).flatMap(i => (0 until y).map(j => (i,j))).toList
  (newLights ::: display).distinct
}
def rotCol(col: Int, by: Int, display: List[(Int, Int)]): List[(Int,Int)] = {
  display.map(i => {
    if(col == i._1) {
      (i._1, (i._2 + by) % ROW)
    } else { i }
  })
}
def rotRow(row: Int, by: Int, display: List[(Int, Int)]): List[(Int,Int)] = {
  display.map(i => {
    if(row == i._2) {
      ((i._1 + by) % COL, i._2)
    } else { i }
  })
}
def doInstruction(instructions: List[String], display: List[(Int,Int)]): List[(Int, Int)] = {
  if(instructions.length == 0){
    return display
  }
  val newDisplay: List[(Int,Int)] = instructions.head match {
    case rectReg(d1,d2) => rect(d1.toInt, d2.toInt, display)
    case rotColReg(d1,d2) => rotCol(d1.toInt, d2.toInt, display)
    case rotRowReg(d1,d2) => rotRow(d1.toInt, d2.toInt, display)
    case _ => {
      println(s"No match...")
      display
    }
  }
  doInstruction(instructions.tail, newDisplay)
}
val code = doInstruction(instructions, List())
println(code.length)

// Part 2
val display = (0 until COL).flatMap(i => (0 until ROW).map(j => (i,j))).toList
val lines = display.groupBy(x => x._2)
for(i <- 0 until ROW) {
  val line: List[String] = lines(i).map(px => if(code.contains(px)){"#"}else{" "})
  val lineStr = line.reduce((acc, curr) => acc + curr)
  println(lineStr)
}
