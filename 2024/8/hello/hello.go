package main

import (
	"fmt"
	"os"
	"strings"

	"example.com/greetings"
)

func main() {
	b, err := os.ReadFile("input_small.txt")
	if err != nil {
		fmt.Print(err)
	}
	// log.SetPrefix("greetings: ")
	// log.SetFlags(0)
	// // Get a greeting message and print it.
	// names := []string{"Gladys", "Samantha", "Darrin"}
	// message, err := greetings.Hellos(names)
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// fmt.Println(b)
	str := string(b)
	stringSlice := strings.Split(str, "\n")
	if len(stringSlice) > 0 {
		stringSlice = stringSlice[:len(stringSlice)-1]
	}
	antenna_locations := make(map[string][][]int)

	height := len(stringSlice)
	width := len(stringSlice[0]) - 1
	fmt.Println("HEIGHT")
	fmt.Println(height)
	for row, line := range stringSlice {
		for column, entry := range line {
			if string(entry) != "." {
				coordinates := [2]int{row, column}
				val, ok := antenna_locations[string(entry)]
				if ok {

					val = append(val, coordinates[:])
					antenna_locations[string(entry)] = val
				} else {
					antenna_locations[string(entry)] = [][]int{coordinates[:]}
				}
				// fmt.Println(string(entry))
			}
			// fmt.Println(row)
			// fmt.Println(line)
			// fmt.Println(column)
		}

	}
	// fmt.Println(antenna_locations["P"])
	antinode_locations := [][]int{}
	for _, locations := range antenna_locations {
		num_of_locations := len(locations)
		for first := range num_of_locations - 1 {
			second_slice := []int{first + 1}
			for quick_index := range num_of_locations {
				if quick_index > first+1 {
					second_slice = append(second_slice, quick_index)
				}
			}
			for _, second := range second_slice {
				dx := locations[second][0] - locations[first][0]
				dy := locations[second][1] - locations[first][1]
				first_antenna := []int{0, 0}
				first_antenna[0] = locations[second][0] + dx
				first_antenna[1] = locations[second][1] + dy
				second_antenna := []int{0, 0}
				second_antenna[0] = locations[second][0] - dx
				second_antenna[1] = locations[second][1] - dy
				// fmt.Println(first_antenna)

				antinode_locations = greetings.AddAntinode(first_antenna, antinode_locations, height, width)
				antinode_locations = greetings.AddAntinode(second_antenna, antinode_locations, height, width)

				// fmt.Println(antinode_locations)
			}
		}
	}
	// fmt.Println(antinode_locations)
	fmt.Println(len(antinode_locations))
}
