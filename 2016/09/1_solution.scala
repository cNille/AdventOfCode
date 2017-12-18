val line = scala.io.Source.fromFile("data.txt").getLines.toList(0)

case class Result(processed: String, toProcess: String)
val decompReg = """\((\d+)x(\d+)\)(.*)""".r

def repeats(l: Int, rep: Int, rest: String, processed: String): Result = {
  val toRepeat = rest.substring(0, l)
  val tail = rest.substring(l)
  val repeat = (1 to rep).map(x => toRepeat).mkString
  Result(processed + repeat, tail)
}

def decompress(res: Result): Result = {
  if(res.toProcess.length == 0){
    return res
  }
  res.toProcess match {
    case decompReg(l, rep, rest) => decompress(repeats(l.toInt, rep.toInt, rest, res.processed))
    case _ => decompress(Result(res + line.head.toString, line.tail))
  }
}

val wow = decompress(Result("", line))
println(wow.processed.length)
