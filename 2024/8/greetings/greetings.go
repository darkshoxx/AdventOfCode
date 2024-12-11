package greetings

import (
	"errors"
	"fmt"
	"math/rand"
)

// Hello returns a greeting for the named person.
func Hello(name string) (string, error) {
	// If no name was given, return an error with a message.
	if name == "" {
		return "", errors.New("empty name")
	}

	// If a name was received, return a value that embeds the name
	// in a greeting message.
	message := fmt.Sprintf(randomFormat(), name)
	return message, nil
}

func AddAntinode(antinode []int, antinode_locations [][]int, height int, width int) [][]int {
	if 0 <= antinode[0] && antinode[0] < height && 0 <= antinode[1] && antinode[1] < width {

		// fmt.Println(antinode[0])
		// fmt.Println(width)
		// fmt.Println(antinode[1] < width)
		contains := false
		for _, location := range antinode_locations {
			both := false
			both = location[0] == antinode[0]
			both = both && location[1] == antinode[1]

			if both {
				contains = true
			}
		}
		if !contains {
			antinode_locations = append(antinode_locations, antinode)
		}
	}
	return antinode_locations
}

func Hellos(names []string) (map[string]string, error) {
	messages := make(map[string]string)
	for _, name := range names {
		message, err := Hello(name)
		if err != nil {
			return nil, err
		}
		messages[name] = message
	}
	return messages, nil
}

func randomFormat() string {
	formats := []string{
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hail, %v! Well met!",
	}
	return formats[rand.Intn(len(formats))]
}