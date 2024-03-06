package main

import "fmt"

func main() {
	Solution("hallo")
	SolutionBetterSolution("hallo")
}

func Solution(word string) string {
	runes := []rune(word)
	size := len(runes)
	for i, j := 0, size-1; i < size>>1; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	fmt.Println(string(runes))
	return string(runes)

}

func SolutionBetterSolution(word string) (reversed string) {
	for _, char := range word {
		reversed = string(char) + reversed
	}
	fmt.Printf(reversed)
	return
}
