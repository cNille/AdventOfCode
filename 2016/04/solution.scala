//Part 1
val roomReg = """([a-z-]*)([0-9]*)\[([\w]*)\]""".r
val list = scala.io.Source.fromFile("data.txt").getLines
  .map( x => x match {
      case roomReg(s1,s2,s3) => List(s1,s2,s3)
    } )
  .filter( s =>
    s(2)  == s(0).filter(_!='-').groupBy(identity)
      .mapValues(_.size).toSeq
      .sortWith((a, b) => a._2 > b._2 || a._2 == b._2 && a._1 < b._1)
      .map(_._1).mkString.substring(0,5)
  )
//val result = list.foldLeft(0){ (acc, curr) => { acc + curr(1).toInt } }
//println(s"result: $result")

// Part 2
def decrypt(str: String, shift: Int) :String = {
  str.toUpperCase.map( x => 
    if(x == '-') { ' ' } else {
      val t = (x.toInt - 65 + (shift % 26)) % 26
      (t + 65 + (if(t < 0){ 26 }else{ 0 })).toChar
    }
  )
}

list.foreach { x => 
  val d = decrypt(x(0), x(1).toInt)
  val id = x(1)
  println(s"$id   - $d")
}
// To get answer. Run with; 
//    scala solution.scala | grep 'NORTH' 
