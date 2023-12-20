package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Box struct {
	labelToIdx map[string]int
	values     []int
}

func addLens(box *Box, value int, label string) {
	_, ok := box.labelToIdx[label]
	if ok {
		// Replace
		box.values[box.labelToIdx[label]] = value
	} else {
		// Add
		box.values = append(box.values, value)
		box.labelToIdx[label] = len(box.values) - 1
	}
}

func removeLens(box *Box, label string) {
	idx, ok := box.labelToIdx[label]
	if ok {
		// Remove
		box.values = append(box.values[:idx], box.values[idx+1:]...)
		delete(box.labelToIdx, label)
		for k, v := range box.labelToIdx {
			if v > idx {
				box.labelToIdx[k] = v - 1
			}
		}
	}
}

func printBoxes(boxes []Box) {
	for _, box := range boxes {
		if len(box.values) != 0 {
			fmt.Println("Box:", box)
		}
	}
}

func readFile(file string) []string {
	fileHandle, err := os.Open(file)
	if err != nil {
		log.Fatal(err)
	}
	defer fileHandle.Close()

	data := make([]string, 0)
	scanner := bufio.NewScanner(fileHandle)
	for scanner.Scan() {
		line := scanner.Text()
		values := strings.Split(line, ",")
		data = append(data, values...)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return data
}

func hashAlgorithm(s string) uint64 {
	var result uint64 = 0
	//Determine the ASCII code for the current character of the string.
	//Increase the current value by the ASCII code you just determined.
	//Set the current value to itself multiplied by 17.
	//Set the current value to the remainder of dividing itself by 256.

	for _, v := range s {
		result += uint64(uint8(v))
		result *= 17
		result = result % 256
	}
	return result
}

func main() {
	data := readFile("input.txt")
	//fmt.Println(data)

	// Make a list of 255 boxes
	boxes := make([]Box, 256)

	// Init boxes
	for i := 0; i < 256; i++ {
		boxes[i] = Box{
			labelToIdx: make(map[string]int),
			values:     make([]int, 0),
		}
	}

	for _, v := range data {
		//fmt.Println("Iter:", index)
		if strings.Contains(v, "=") {
			// Split by "="
			parts := strings.Split(v, "=")

			//fmt.Println("Key:", parts[0], "Value:", parts[1])
			label := parts[0]
			id := hashAlgorithm(parts[0])
			value, _ := strconv.Atoi(parts[1])

			addLens(&boxes[id], value, label)
		} else if strings.Contains(v, "-") {
			// Split by "-"
			parts := strings.Split(v, "-")

			//fmt.Println("Key:", parts[0])

			label := parts[0]
			id := hashAlgorithm(parts[0])
			removeLens(&boxes[id], label)
		}
		//printBoxes(boxes)
	}
	focusingPower := 0

	for box_idx, box := range boxes {
		for i, value := range box.values {
			fmt.Printf("Box: %d, Lens: %d, Value: %d\n", box_idx, i, value)
			focusingPower += (box_idx + 1) * (i + 1) * value
		}
	}
	fmt.Println("Focusing power:", focusingPower)
}
