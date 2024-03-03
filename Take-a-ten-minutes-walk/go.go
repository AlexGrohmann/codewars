package main

import (
	"fmt"
)

func main() {
	IsValidWalk([]rune{'n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'})
	IsValidWalk([]rune{'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'})
	IsValidWalk([]rune{'w'})
	IsValidWalk([]rune{'n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's'})
	IsValidWalk([]rune{'e', 'e', 'e', 'e', 'w', 'w', 's', 's', 's', 's'})
}

func IsValidWalk(walk []rune) bool {
	var countN int
	var countS int
	var countE int
	var countW int
	for _, val := range walk {
		switch string(val) {
		case "n":
			countN++
		case "s":
			countS++
		case "e":
			countE++
		case "w":
			countW++
		}
	}
	fmt.Println((countN == countS) && (countW == countE) && (len(walk) == 10))
	return (countN == countS) && (countW == countE) && (len(walk) == 10)
}
