// problem 46
package main

import (
	"euler/lib"
	"fmt"
)

const powersize = 1000

func main() {
	primes := lib.EratosthenesSieve(200000)
	powers := make([]int, powersize)

	// make powers array
	for a := 0; a < powersize; a++ {
		powers[a] = 2 * (a + 1) * (a + 1)
	}

	i := 3  // starting point of example
	ip := 2 // index of last prime before i
	for true {
		i += 2

		// advance primes
		for ; primes[ip] < i; ip++ {
		}

		if i != primes[ip] {
			goldbach := false
			for k := ip; k >= 0; k-- {
				for j := 0; j < powersize; j++ {
					if (primes[k] + powers[j]) == i {
						goldbach = true
						break
					}
				}
				if goldbach {
					break
				}
			}
			if !goldbach {
				fmt.Println(i)
				break
			}
		}
	}
}
