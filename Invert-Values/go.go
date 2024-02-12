package main

import "fmt"

func main() {
	Invert([]int{1, 2, 3, 4, 5})
}

func Invert(arr []int) []int {
	println("run", arr)
	var result []int
	for _, item := range arr {
		println(item)
		result = append(result, item*-1)
	}
	fmt.Println(result)
	return result
}
