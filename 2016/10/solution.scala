val lines = scala.io.Source.fromFile("data.txt").getLines.toList

case class Result(bots: List[Bot], values: List[Value])
case class Bot(nbr: Int, lowTo: Int, hightTo: Int)
case class Value(values: Int, bot: Int)

val givesReg1 = """bot (\d+) gives low to bot (\d+) and high to bot (\d+)""".r
val givesReg2 = """bot (\d+) gives low to output (\d+) and high to bot (\d+)""".r
val givesReg3 = """bot (\d+) gives low to bot (\d+) and high to output (\d+)""".r
val givesReg4 = """bot (\d+) gives low to output (\d+) and high to output (\d+)""".r
val valueReg = """value (\d+) goes to bot (\d+)"""r

def process(lines: List[String], bots: List[Bot], values: List[Value]):Result = {
  if(lines.length == 0){
    return Result(bots, values)
  }
  val line = lines.head

  val newBots = line match {
    case givesReg1(nbr, lowTo, highTo) => List(Bot(nbr.toInt, lowTo.toInt, highTo.toInt))
    case givesReg2(nbr, lowTo, highTo) => List(Bot(nbr.toInt, -lowTo.toInt, highTo.toInt))
    case givesReg3(nbr, lowTo, highTo) => List(Bot(nbr.toInt, lowTo.toInt, -highTo.toInt))
    case givesReg4(nbr, lowTo, highTo) => List(Bot(nbr.toInt, -lowTo.toInt, -highTo.toInt))
    case _ => List()
  }   
  
  // Check i value line and do some function?? 
  
  process(lines.tail, bots ::: newBots, values)
}

val res = process(lines, List(), List())
println(res)

