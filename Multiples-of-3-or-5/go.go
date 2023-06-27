package main

import "fmt"

func main() {
	Multiple3And5(50)
}

func Multiple3And5(number int) int {
	result := 0
	for i := 0; i < number; i++ {
		if i%3 == 0 || i%5 == 0 {
			result += i
		}
	}
	fmt.Print(result)
	return result
}
