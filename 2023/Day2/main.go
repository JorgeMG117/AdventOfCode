package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
    "io/ioutil"
    "os"

)

type CubeConf struct {
    nRed int
    nBlue int
    nGreen int
}

func main() {

    cubeConf := CubeConf{nRed: 12, nBlue: 14, nGreen: 13}
    fmt.Printf("Cube configuration: Red: %d, Blue: %d, Green: %d\n", cubeConf.nRed, cubeConf.nBlue, cubeConf.nGreen)
    idSum := 0 
    power := 0

    f, err := os.Open("input")
	if err != nil {
		panic(err)
	}

	c, err := ioutil.ReadAll(f)
	if err != nil {
		panic(err)
	}

	//fmt.Printf("### Contenido de archivo: ###\n%s\n", string(c))
	f.Close()

    input := string(c)

	// Split the input into individual games
	games := strings.Split(input, "Game ")

	// Define a regular expression to extract game ID and counts of red, blue, and green items
	reGame := regexp.MustCompile(`(\d+):`)
	reCounts := regexp.MustCompile(`(\d+) (red|blue|green)`)

	// Process each game
	for i, game := range games {
		if i == 0 {
			// Skip the first element, as it's empty
			continue
		}

        minRed := 0
        minBlue := 0
        minGreen := 0

		// Find game ID in the game string
		matchGame := reGame.FindStringSubmatch(game)
		gameID, _ := strconv.Atoi(matchGame[1])

		// Print the game number and ID
		// fmt.Printf("Game %d (ID %d):\n", i, gameID)
	    gameSubsets := strings.Split(game, ";")

        possible := true
        for _, part := range gameSubsets {
            // Find matches for counts in the game string
            matches := reCounts.FindAllStringSubmatch(part, -1)

            // Initialize counters
            redCount := 0
            blueCount := 0
            greenCount := 0

            // Process each match
            for _, match := range matches {
                count, _ := strconv.Atoi(match[1])
                color := match[2]

                // Update counters based on color
                switch color {
                case "red":
                    redCount += count
                    if(minRed < count){
                        minRed = count
                    }
                case "blue":
                    blueCount += count
                    if(minBlue < count){
                        minBlue = count
                    }
                case "green":
                    greenCount += count
                    if(minGreen < count){
                        minGreen = count
                    }
                }
            }
            // Debugging: Print counts for each game


            // Print the counts for the current game
            /*
            fmt.Printf("  Red: %d\n", redCount)
            fmt.Printf("  Blue: %d\n", blueCount)
            fmt.Printf("  Green: %d\n", greenCount)
            fmt.Println()
            */

            if(redCount > cubeConf.nRed || blueCount > cubeConf.nBlue || greenCount > cubeConf.nGreen){
                possible = false
            }
        }
        power = power + minRed * minBlue * minGreen
        if(possible){
            idSum += gameID
        }

	}
    fmt.Println(idSum)
    fmt.Println(power)
}

