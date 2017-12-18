val line = scala.io.Source.fromFile("data.txt").getLines.toList(0)

case class Result(processed: Long, toProcess: String)
val decompReg = """\((\d+)x(\d+)\)(.*)""".r

def repeats(l: Long, rep: Long, rest: String, processed: Long): Result = {
  val toRepeat = decompress(Result(0, rest.substring(0, l.toInt)))
  val tail = rest.substring(l.toInt)
  val repeat = toRepeat.processed * rep 
  Result(processed + repeat, tail)
}

def decompress(res: Result): Result = {
  if(res.toProcess.length == 0){
    return res
  }
  res.toProcess match {
    case decompReg(l, rep, rest) => decompress(repeats(l.toInt.toLong, rep.toInt.toLong, rest, res.processed))
    case _ => decompress(Result(res.processed + 1, res.toProcess.tail))
  }
}

val wow = decompress(Result(0, line))
println(wow.processed)
