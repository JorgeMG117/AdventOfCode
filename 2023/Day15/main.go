package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

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
	fmt.Println(data)

	var result uint64 = 0
	for _, v := range data {
		result += hashAlgorithm(v)
	}
	fmt.Println(result)
}
