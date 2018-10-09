package main

import (
	"fmt"
)

func main() {

	var n int
	fmt.Scanf("%d", &n)
	for i := 0; i < n; i++ {
		var a int
		fmt.Scanf("%d", &a)
		if a%2 == 0 {
			fmt.Println(a, "is even")
		} else {
			fmt.Println(a, "is odd")
		}
	}
}
