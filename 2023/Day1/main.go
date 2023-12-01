package main

import (
    "os"
    "bufio"
    "strconv"
)


func check(e error) {
    if e != nil {
        panic(e)
    }
}


func main() {
    // Read file line by line
    //Search for the first occurence of a number
    //Search second occurence of a number or end of line

    f, err := os.Open("example.txt")
    check(err)

    scanner := bufio.NewScanner(f)
    var sum int = 0
    for scanner.Scan() {
        line := scanner.Text()
        var first string = ""
        var second string = ""
        for i := 0; i < len(line); i++ {
            if line[i] >= '0' && line[i] <= '9' {
                first = string(line[i])
                for j := len(line) - 1; j >= i; j-- {
                    if line[j] >= '0' && line[j] <= '9' {
                        second = string(line[j])
                        //Sum the two numbers
                        firstInt, err := strconv.Atoi(first + "0")
                        check(err)
                        secondInt, err := strconv.Atoi(second)
                        check(err)
                        sum += firstInt + secondInt
                        break
                    }
                }
                break
            }
        }
    }
    println(sum)

}

