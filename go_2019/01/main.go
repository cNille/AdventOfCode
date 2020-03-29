package main

import (
  "bufio"
  "fmt"
  "os"
  "strconv"
)



func part1(s []string) string {
  result := 0 

  for _, v := range s {
    i, _ := strconv.Atoi(v)
    fuel := (i / 3) - 2
    result += fuel 
    fmt.Printf("val: %d, fuel: %d, res: %d", i, fuel, result)
  } 

  return fmt.Sprintf("Result: %d", result)
}


func part2(s []string) string {
  result := 0 

  for _, v := range s {
    i, _ := strconv.Atoi(v)
    fuel := (i / 3) - 2
    result += fuel 
    fmt.Printf("val: %d, fuel: %d, res: %d", i, fuel, result)
  } 

  return fmt.Sprintf("Result: %d", result)
}

}
func main() {
  file, _ := os.Open("01.input")
  defer file.Close()
  fileScanner := bufio.NewScanner(file)

  var lines []string
  for fileScanner.Scan() {
    lines = append(lines, fileScanner.Text())
  }

  fmt.Println(part1(lines))
  fmt.Println(part2(lines))
}
