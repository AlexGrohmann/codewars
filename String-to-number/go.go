package main

import (
	"fmt"
	"strconv"
)

func main() {
	StringToNumber("50")
	StringToNumber("-5")
	StringToNumber("1234")
	StringToNumber("43")
}

func StringToNumber(str string) int {
	number, _ := strconv.Atoi(str)
	fmt.Println(number)
	return number
}
