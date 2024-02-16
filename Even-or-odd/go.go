package main

import "fmt"

func main() {
	EvenOrOdd(50)
}

func EvenOrOdd(number int) string {
	if number%2 == 0 {
		fmt.Print("Even")
		return "Even"
	} else {
		fmt.Print("Odd")
		return "Odd"
	}
}
