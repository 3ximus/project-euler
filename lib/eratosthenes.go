package main

import (
	"fmt"
	"math"
	"time"
)

func sum(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}

func SieveBasic(n int) []int {
	// n+1 allows us to start the loop at 2
	// without a subtracting 2 from each iteration
	// (this just ignores indexes 0, 1)
	marks := make([]bool, n+1)
	//preallocate the array; upper bound of half (no even numbers > 2)
	primes := make([]int, n/2)
	pi := 0
	for i := 2; i <= n; i++ {
		if marks[i] {
			continue
		}
		primes[pi] = i
		pi++
		// walk the array by increments of the current value
		// eliminating all multiples of i
		for m := i; m <= n; m += i {
			marks[m] = true
		}
	}
	return primes[:pi]
}

func Sieve2(n int) []int {
	marks := make([]bool, n/2+1)
	primes := make([]int, n/2+1)
	pi := 0

	if n <=1 {
		return make([]int, 0);
	}

	for i := 3; i <= int(math.Sqrt(float64(n))); i+=2 {
		if !marks[i/2] {
			for m := i*i/2; m <= n/2; m += i {
				marks[m] = true
			}
		}
	}

	for i := 0; i < int(math.Ceil(float64(n)/2)); i++ {
		if !marks[i] {
			primes[pi] = 2 * i + 1;
			pi++;
		}
	}
	primes[0] = 2;
	return primes[:pi]
}

func main() {
	start := time.Now();
	fmt.Printf("Sieve Basic %v\n %v\n", sum(SieveBasic(20000000)), time.Since(start));
	start = time.Now();
	fmt.Printf("Sieve Half Squared %v\n %v\n", sum(Sieve2(20000000)), time.Since(start));
}
