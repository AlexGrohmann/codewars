package main

import "fmt"

func main() {
	Multiply(50, 2)
}

func Multiply(a, b int) int {
	fmt.Println(a * b)
	return a * b
}
