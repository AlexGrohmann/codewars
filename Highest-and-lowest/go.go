package kata

import (
	"strconv"
	"strings"
)

func HighAndLow(in string) string {
	parts := strings.Split(in, " ")
	max, _ := strconv.Atoi(parts[0])
	min, _ := strconv.Atoi(parts[0])
	outputMax := parts[0]
	outputMin := parts[0]

	for i := 0; i < len(parts); i++ {
		input, _ := strconv.Atoi(parts[i])
		if max < input {
			max = input
			outputMax = parts[i]
		}

		if min > input {
			min = input
			outputMin = parts[i]
		}
	}

	return outputMax + " " + outputMin
}
