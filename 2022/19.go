package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"time"
)

const MAX_T = 32

func timer(name string) func() {
	start := time.Now()
	return func() {
		fmt.Printf("%s took %v\n", name, time.Since(start))
	}
}

func inc_robot(blueprint [7]int, state [9]int, r int) [9]int {
	if r == 0 { // ORE
		state[1] += 1
		state[5] -= blueprint[1]
	} else if r == 1 { // CLAY
		state[2] += 1
		state[5] -= blueprint[2]
	} else if r == 2 { // OBSIDIAN
		state[3] += 1
		state[5] -= blueprint[3]
		state[6] -= blueprint[4]
	} else if r == 3 { // GEODE
		state[4] += 1
		state[5] -= blueprint[5]
		state[7] -= blueprint[6]
	}
	return state
}

func inc_resources(state [9]int) [9]int {
	state[5] += state[1]
	state[6] += state[2]
	state[7] += state[3]
	state[8] += state[4]
	return state
}

func game(blueprint [7]int, state [9]int) [][9]int {
	// Increase time
	state[0] = state[0] + 1
	new_states := [][9]int{}

	// -- Can purchase robot
	can_purchase := [4]bool{true, true, true, true}
	can_purchase[0] = blueprint[1] <= state[5]
	can_purchase[1] = blueprint[2] <= state[5]
	can_purchase[2] = blueprint[3] <= state[5] && blueprint[4] <= state[6]
	can_purchase[3] = blueprint[5] <= state[5] && blueprint[6] <= state[7]

	// Increase resources
	new_state := inc_resources(state)

	// Get 2 first purchases.
	purchase := []int{}
	for i, v := range can_purchase {
		if v {
			purchase = append(purchase, i)
		}
	}

	// Only purchase ORE with another thing simultanously
	//if len(purchase) > 2 {
	//	new_purchase := []int{}
	//	new_purchase = append(new_purchase, purchase[0])
	//	new_purchase = append(new_purchase, purchase[len(purchase)-1])
	//	purchase = new_purchase
	//}

	for _, p := range purchase {
		new_state2 := inc_robot(blueprint, new_state, p)
		new_states = append(new_states, new_state2)
	}

	// Purchase nothing (if one cannot buy geode)
	if !can_purchase[3] {
		new_states = append(new_states, new_state)
	}
	return new_states
}

// State values:
// 0: TIME
// 1: ROBOT ORE
// 2: ROBOT CLAY
// 3: ROBOT OBSIDIAN
// 4: ROBOT GEODE
// 5: RESOURCE ORE
// 6: RESOURCE CLAY
// 7: RESOURCE OBSIDIAN
// 8: RESOURCE GEODE

func use_blueprint(blueprint [7]int) int {
	defer timer("use_blueprint")()
	init_state := [9]int{0, 1, 0, 0, 0, 0, 0, 0, 0}
	max_geodes := [MAX_T]int{}

	levels := [MAX_T][][9]int{}

	t := 0
	levels[t] = append(levels[t], init_state)
	for {
		max_geode := 0
		start := time.Now()
		reach := map[[9]int]bool{}
		for _, nxt := range levels[t] {
			if nxt[0] > MAX_T {
				continue
			}
			_, ok := reach[nxt]
			if ok {
				continue
			}
			reach[nxt] = true
			new_states := game(blueprint, nxt)
			for _, state := range new_states {
				if t+1 < MAX_T {
					if t > 10 {
						if state[8] >= max_geodes[t-2] {
							levels[t+1] = append(levels[t+1], state)
						}
					} else {
						levels[t+1] = append(levels[t+1], state)
					}
				}
				if state[8] > max_geode {
					max_geode = state[8]
				}
			}
			max_geodes[t] = max_geode
		}
		fmt.Printf("T=%d took %v, with max: %d \n", t+1, time.Since(start), max_geodes[t])
		t = t + 1
		if t >= MAX_T {
			break
		}
	}

	fmt.Println(max_geodes)
	return max_geodes[MAX_T-1]
}

func main() {
	fmt.Println("Day 19")
	//content, err := os.ReadFile("19.test")
	content, err := os.ReadFile("19.input")
	if err != nil {
		panic(err)
	}
	re, err := regexp.Compile(`\d+`)
	if err != nil {
		panic(err)
	}
	blueprintData := strings.Split(string(content), "\n")
	blueprints := [][7]int{}
	for _, b := range blueprintData {
		if b == "" {
			continue
		}
		matches := re.FindAll([]byte(b), 7)
		if err != nil {
			panic(err)
		}

		b := [7]int{}
		for i, m := range matches {
			v, err := strconv.Atoi(string(m))
			if err != nil {
				panic(err)
			}
			b[i] = int(v)
		}
		blueprints = append(blueprints, b)
	}
	// max_geode := use_blueprint(blueprints[1])
	// fmt.Println("Finished with", 2, ":", max_geode)

	i := 0
	result := 1
	for i < 3 {
		max_geode := use_blueprint(blueprints[i])
		fmt.Println("Finished with", i, ":", max_geode)
		result = result * max_geode

		i += 1
	}
	fmt.Println("Solution part 2:", result)
}

// T 31
// 4320 too low  (24*18*10)
// 5184 too low (24*18*12)

// T 32
// 9338 too low (29*23*14)
