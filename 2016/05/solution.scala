import java.lang.StringBuilder
val md = java.security.MessageDigest.getInstance("MD5")
def hash(str: String): String = md.digest(str.getBytes).map("%02x".format(_)).mkString
val start = System.currentTimeMillis()



// Part 1
def encrypt1(str: String, i: Int, curr: String): String = {
  if(curr.length >= 8) { curr }
  if(i % 100000 == 0){
    val time = (System.currentTimeMillis() - start) / 1000
    println(s"Encrypting $i... Time passed: $time seconds.  Current pw: $curr")
  }

  val h = hash(str + i)
  val res = if(h.substring(0,5) == "00000"){ curr + h(5) } else { curr }
  encrypt1(str, i + 1, res)
}
// Part 2
def encrypt2(str: String, i: Int, curr: String): String = {
  if(curr.indexOf('-') < 0) { curr }
  if(i % 100000 == 0){
    val time = (System.currentTimeMillis() - start) / 1000
    println(s"Encrypting $i... Time passed: $time seconds.  Current pw: $curr")
  }

  val h = hash(str + i)
  val res = if(h.substring(0,5) == "00000"){
    println("Hej:" + h(5) + ", " + h(6))
    val sb = new StringBuilder(curr)
    if(h(5).asDigit < 8 && curr(h(5).asDigit) == '-'){ 
      sb.setCharAt(h(5).asDigit, h(6))
    }
    sb.toString
  } else { curr }
  encrypt2(str, i + 1, res)
}

val input = "cxdnnyjw"
val pw = encrypt2(input, 2500000, "--------")

println(s"Password is: $pw")


