package main

import (
	"fmt"
	"math"
)

func main() {
	HumanReadableTime(45296)
}

func HumanReadableTime(seconds int) string {
	hoursLeft := math.Floor(float64(seconds) / 3600)
	min := math.Floor((float64(seconds) - hoursLeft*3600) / 60)
	secondsLeft := float64(seconds) - hoursLeft*3600 - min*60
	secondsLeft = math.Round((float64(secondsLeft) * 100) / 100)
	hhString := fmt.Sprintf("%d", int(hoursLeft))
	mmString := fmt.Sprintf("%d", int(min))
	ssString := fmt.Sprintf("%d", int(secondsLeft))
	if len(hhString) < 2 {
		hhString = "0" + hhString
	}
	if len(mmString) < 2 {
		mmString = "0" + mmString
	}
	if len(ssString) < 2 {
		ssString = "0" + ssString
	}
	fmt.Println(hhString + ":" + mmString + ":" + ssString)
	return hhString + ":" + mmString + ":" + ssString
}
