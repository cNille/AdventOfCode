package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"time"
)

func main() {
	dat, err := ioutil.ReadFile("my.input")
	check(err)
	lines := strings.Split(string(dat), "\n")
	//solution1(lines)
	solution2(lines)
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}
func get_value(reg map[string]int, value string) int {
	if val, ok := reg[value]; ok {
		return val
	}
	v1, err := strconv.Atoi(value)
	check(err)
	return v1
}

func solution1(lines []string) {
	reg := map[string]int{"a": 0, "p": 0, "b": 0, "f": 0, "i": 0}
	stack := []int{}
	i := -1
	is_done := false
	for i < len(lines) && !is_done {
		i += 1
		l := strings.Split(lines[i], " ")
		fmt.Println(i, l, reg)

		switch l[0] {
		case "set":
			reg[l[1]] = get_value(reg, l[2])
		case "add":
			reg[l[1]] += get_value(reg, l[2])
		case "mul":
			reg[l[1]] *= get_value(reg, l[2])
		case "mod":
			reg[l[1]] %= get_value(reg, l[2])
		case "snd":
			stack = append(stack, get_value(reg, l[1]))
		case "rcv":
			fmt.Println("Result", stack[len(stack)-1])
			is_done = true
		case "jgz":
			if get_value(reg, l[1]) > 0 {
				i += get_value(reg, l[2]) - 1
			}
		}
	}
}
func solution2(lines []string) {
	c1 := make(chan int, 1000)
	c2 := make(chan int, 1000)

	go program(lines, 0, c1, c2)
	go program(lines, 1, c2, c1)
	time.Sleep(time.Millisecond * 4000)
	fmt.Println("===============Time end===============")
}
func program(lines []string, programId int, recieve chan int, send chan int) {
	reg := map[string]int{"a": 0, "p": programId, "b": 0, "f": 0, "i": 0}
	count := 0

	for i := 0; i < (len(lines) - 1); i++ {
		l := strings.Split(lines[i], " ")

		switch l[0] {
		case "set":
			reg[l[1]] = get_value(reg, l[2])
		case "add":
			reg[l[1]] += get_value(reg, l[2])
		case "mul":
			reg[l[1]] *= get_value(reg, l[2])
		case "mod":
			reg[l[1]] %= get_value(reg, l[2])
		case "snd":
			count += 1
			if programId == 1 {
				fmt.Println(programId, "count", count)
			}
			send <- get_value(reg, l[1])
		case "rcv":
			reg[l[1]] = <-recieve
		case "jgz":
			if get_value(reg, l[1]) > 0 {
				i += get_value(reg, l[2]) - 1
			}
		}
	}
}
