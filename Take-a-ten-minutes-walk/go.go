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
		switch val {
		case 'n':
			countN++
		case 's':
			countS++
		case 'e':
			countE++
		case 'w':
			countW++
		}
	}
	fmt.Println((countN == countS) && (countW == countE) && (len(walk) == 10))
	return (countN == countS) && (countW == countE) && (len(walk) == 10)
}

func IsValidWalkNiceSolution(walk []rune) bool {
	if len(walk) != 10 {
		return false
	}

	x, y := 0, 0
	for _, r := range walk {
		switch r {
		case 'n':
			y++
		case 's':
			y--
		case 'e':
			x++
		case 'w':
			x--
		}
	}

	if x == 0 && y == 0 {
		return true
	}

	return false
}
