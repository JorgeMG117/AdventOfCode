package main

import (
    "fmt"
    "bufio"
    "os"
)

type Position struct {
    posX int
    posY int
}

var right = Position{1, 0}
var left = Position{-1, 0}
var up = Position{0, -1}
var down = Position{0, 1}


type Cavern struct {
    cavern []string
    energizedTiles map[Position]bool
}

func (cavern *Cavern) Print() {
    for _, row := range cavern.cavern {
        fmt.Println(row)
    }
}

// empty space (.), mirrors (/ and \), and splitters (| and -).
func initializeCavern(fileName string) (Cavern, error) {
    // Read file
    file, err := os.Open(fileName)
    if err != nil {
        return Cavern{}, err
    }
    defer file.Close()

    /*
    var matrix [][]int

    // Create a new scanner and read the file line by line
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        var row []int
        // Split each line into elements
        for _, elem := range strings.Fields(scanner.Text()) {
            // Convert string to int
            num, err := strconv.Atoi(elem)
            if err != nil {
                fmt.Println(err)
                return Cavern{}, err
            }
            row = append(row, num)
        }
        // Append the row to the matrix
        matrix = append(matrix, row)
    }

    if err := scanner.Err(); err != nil {
        fmt.Println(err)
        return
    }
    */
    var matrix []string

    // Create a new scanner and read the file line by line
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        // Append the line (row of the matrix) to the matrix
        matrix = append(matrix, scanner.Text())
    }

    if err := scanner.Err(); err != nil {
        return Cavern{}, err
    }

    cavern := Cavern{matrix, make(map[Position]bool)}
    
    return cavern, nil
}


func changeDirection(direction Position, mirror string) Position {
    if mirror == "/" {
        if direction == right {
            return up
        } else if direction == left {
            return down
        } else if direction == up {
            return right
        } else if direction == down {
            return left
        }
    } else {
        if direction == right {
            return down
        } else if direction == left {
            return up
        } else if direction == up {
            return left
        } else if direction == down {
            return right
        }
    }
    return direction
}

func changeSplitter(direction Position, splitter string) []Position {
    //fmt.Println("Current direction: ")
    //fmt.Println(direction)
    if splitter == "|" {
        if direction == right {
            return []Position{up, down}
        } else if direction == left {
            return []Position{up, down}
        } else if direction == up {
            return []Position{up}
        } else if direction == down {
            return []Position{down}
        }
    } else {
        if direction == right {
            return []Position{right}
        } else if direction == left {
            return []Position{left}
        } else if direction == up {
            return []Position{left, right}
        } else if direction == down {
            return []Position{left, right}
        }
    }
    return []Position{direction}
}

func trakingBeam(cavern *Cavern, position Position, direction Position) {
    if _, ok := cavern.energizedTiles[position]; ok {
        return
    }
    // if outside of cavern return
    if position.posX < 0 || position.posX >= len(cavern.cavern[0]) || position.posY < 0 || position.posY >= len(cavern.cavern) {
        //fmt.Println("Out of bounds")
        return
    }

    // if empty go same direction
    if cavern.cavern[position.posY][position.posX] == '.' {
        //fmt.Println("Empty")
        cavern.energizedTiles[position] = true
        position.posX += direction.posX
        position.posY += direction.posY
        trakingBeam(cavern, position, direction)

    } else if cavern.cavern[position.posY][position.posX] == '/' || cavern.cavern[position.posY][position.posX] == '\\' {
        //fmt.Println("Mirror")
        cavern.energizedTiles[position] = true
        //fmt.Println("Current position: ")
        //fmt.Println(position)
        direction = changeDirection(direction, string(cavern.cavern[position.posY][position.posX]))
        //fmt.Println("New direction: ")
        //fmt.Println(direction)
        position.posX += direction.posX
        position.posY += direction.posY
        //fmt.Println("New position: ")
        //fmt.Println(position)
        //fmt.Println("New character: ")
        //fmt.Println(cavern.cavern[position.posY][position.posX])
        trakingBeam(cavern, position, direction)

    } else if cavern.cavern[position.posY][position.posX] == '|' || cavern.cavern[position.posY][position.posX] == '-' {
        //fmt.Println("Splitter")

        cavern.energizedTiles[position] = true
        directions := changeSplitter(direction, string(cavern.cavern[position.posY][position.posX]))
        //fmt.Println("Directions: ")
        //fmt.Println(directions)
        iniPosX := position.posX
        iniPosY := position.posY
        for _, dir := range directions {
            position.posX = iniPosX + dir.posX
            position.posY = iniPosY + dir.posY
            trakingBeam(cavern, position, dir)
        }
    }

    return

}

func main() {
    cavern, err := initializeCavern("example.txt")
    if err != nil {
        fmt.Println(err)
        return
    }

    cavern.Print()

    trakingBeam(&cavern, Position{0, 0}, right)

    fmt.Println(len(cavern.energizedTiles))
}
