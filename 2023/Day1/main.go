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

//Recives, line, and position in line
// Check if the character is a number or if its a number written in words
/*
func isNumber(line string, pos int) (bool, string) {
    lineLen := len(line)
    if line[pos] >= '0' && line[pos] <= '9' {
        return true, string(line[pos]) 
    } else if lineLen > pos + 3  && line[pos] == 'o' && line[pos + 1] == 'n' && line[pos + 2] == 'e' {
        return true, "1"
    } else if lineLen > pos + 3 && line[pos] == 't' && line[pos + 1] == 'w' && line[pos + 2] == 'o' {
        return true, "2"
    } else if lineLen > pos + 5 && line[pos] == 't' && line[pos + 1] == 'h' && line[pos + 2] == 'r' && line[pos + 3] == 'e' && line[pos + 4] == 'e' {
        return true, "3"
    } else if lineLen > pos + 4 && line[pos] == 'f' && line[pos + 1] == 'o' && line[pos + 2] == 'u' && line[pos + 3] == 'r' {
        return true, "4"
    } else if lineLen > pos + 4 && line[pos] == 'f' && line[pos + 1] == 'i' && line[pos + 2] == 'v' && line[pos + 3] == 'e' {
        return true, "5"
    } else if lineLen > pos + 3 && line[pos] == 's' && line[pos + 1] == 'i' && line[pos + 2] == 'x' {
        return true, "6"
    } else if lineLen > pos + 5 && line[pos] == 's' && line[pos + 1] == 'e' && line[pos + 2] == 'v' && line[pos + 3] == 'e' && line[pos + 4] == 'n' {
        return true, "7"
    } else if lineLen > pos + 5 && line[pos] == 'e' && line[pos + 1] == 'i' && line[pos + 2] == 'g' && line[pos + 3] == 'h' && line[pos + 4] == 't' {
        return true, "8"
    } else if lineLen > pos + 4 && line[pos] == 'n' && line[pos + 1] == 'i' && line[pos + 2] == 'n' && line[pos + 3] == 'e' {
        return true, "9"
    }
    return false, ""
}
*/
func isNumber(line string, pos int) (bool, string) {
	lineLen := len(line)
	if line[pos] >= '0' && line[pos] <= '9' {
		return true, string(line[pos])
	}

	wordNumbers := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	for word, digit := range wordNumbers {
		wordLen := len(word)
		if lineLen > pos+wordLen && line[pos:pos+wordLen] == word {
			return true, digit
		}
	}

	return false, ""
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
        var first string
        var second string
        for i := 0; i < len(line); i++ {
            isNum, num := isNumber(line, i)
            if isNum {
                first = num
                for j := len(line) - 1; j >= i; j-- {
                    isNum, num := isNumber(line, j)
                    if isNum {
                        second = num
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

