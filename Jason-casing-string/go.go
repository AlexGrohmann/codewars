package main

import (
	"fmt"
	"unicode"
)

func main() {
	ToJadenCase("How can mirrors be real if our eyes aren't real")
}

func ToJadenCase(input string) string {
	var result []rune
	for pos, val := range input {
		if pos == 0 || string(input[pos-1]) == " " {

			result = append(result, unicode.ToUpper(val))
		} else {

			result = append(result, unicode.ToLower(val))
		}

	}
	fmt.Println(string(result))
	return string(result)
}
