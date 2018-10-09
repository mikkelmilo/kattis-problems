package main

import (
	"fmt"
	"math"
)

func main() {

	var h, v float64
	fmt.Scanf("%f%f", &h, &v)
	res := h / math.Sin(v*math.Pi/180)
	fmt.Println(math.Ceil(res))
}
