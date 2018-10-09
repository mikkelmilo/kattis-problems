package main

import (
	"fmt"
)

func main() {

	var a, b, c, d int
	fmt.Scanf("%d%d%d%d", &a, &b, &c, &d)
	x := []int{a, b, c, d}
	smallest := a
	second_smallest := a
	largest := a
	second_largest := a
	for i, v := range x {
		if v < smallest {
			smallest = v
		}
		if v > largest {
			largest = v
		}
	}
}
