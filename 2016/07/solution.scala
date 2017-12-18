val ips = scala.io.Source.fromFile("data.txt").getLines.toList

// Part 1
// =====================
def splitToInsideAndOutside(ip: String): (List[String], List[String]) =  {
  ip.split("]").foldLeft((List[String](), List[String]())){
    (acc, curr) =>
      val a = curr.split('[')
      (a(0) :: acc._1, if(a.length > 1){ a(1) :: acc._2 } else { acc._2 }) 
  }
}
def isABBA(str: String):Boolean = {
  if(str.length < 4) {
    false
  } else { 
    (str.substring(0,2) == str.substring(2,4).reverse && str(0) != str(1)) || isABBA(str.tail)
  }
} 
def validABBA(ip: String):Boolean = {
  val (out, in) = splitToInsideAndOutside(ip)
  val fOut = out.filter(isABBA)
  val fIn = in.filter(isABBA)
  return fOut.length > 0 && fIn.length == 0
}

// Part 2
// =====================
def triplets(s: String):List[String] = {
  if(s.length < 3) {
    List()
  } else {
    s.substring(0,3) :: triplets(s.tail)
  }
}

def invert(s: String):String = {
  val x = s.substring(0,1)
  val y = s.substring(1,2)
  y + x + y
}

def validABA(str: String):Boolean = {
  val (out, in) = splitToInsideAndOutside(str)
  val inBAB: List[String] = in.flatMap(triplets)
  val outABA: List[String] = out.flatMap(triplets)
  val valid = inBAB.filter( x =>{   
    x(0) == x(2) && 
    x(0) != x(1) && 
    outABA.contains(invert(x)) 
  })
  return valid.length > 0
} 

// Print result
// =====================
val validIps = ips.filter(validABA)
println(validIps.size)
