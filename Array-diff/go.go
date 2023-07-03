package main

import "fmt"

func main() {
	ArrayDiff([]int{1, 2}, []int{1})
}

func ArrayDiff(a, b []int) []int {
	// your code here
	var result []int
	for _, valA := range a {
		set := false
		for _, valB := range b {
			if valA == valB {
				set = true
			}
		}
		if !set {
			result = append(result, int(valA))
		}
	}
	fmt.Println(result)
	return result
}
