package main

import (
	"fmt"
)

func main() {

	x := 0
	y := 0
	for i := 1; i <= 5; i++ {
		var a, b, c, d int
		fmt.Scanf("%d%d%d%d", &a, &b, &c, &d)
		if (a + b + c + d) >= x {
			x = a + b + c + d
			y = i
		}
	}
	fmt.Println(y, x)
}
