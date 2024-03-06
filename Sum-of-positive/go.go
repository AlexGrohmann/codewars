package main

func PositiveSum(numbers []int) int {
	result := 0
	for _, item := range numbers {
		if item > 0 {
			result += item
		}
	}
	return result
}
