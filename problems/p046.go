package main

import (
	"euler/lib"
	"fmt"
)

const POWERSIZE = 1000;

func main() {
	primes := lib.EratosthenesSieve(200000);
	powers := make([]int, POWERSIZE);

	// make powers array
	for a := 0; a < POWERSIZE ; a++ {
		powers[a] = 2 * (a+1) * (a+1);
	}

	i := 3; // starting point of example
	ip := 2; // index of last prime before i
	for true {
		i += 2;
		for ; primes[ip] < i; ip++ {} // advance primes

		if i != primes[ip] {
			goldbach := false;
			for k := ip; k >= 0 ; k-- {
				for j := 0 ; j < POWERSIZE; j++ {
					if (primes[k] + powers[j]) == i {
						goldbach = true;
						break;
					}
				}
				if goldbach {break}
			}
			if !goldbach {
				fmt.Println(i);
				break;
			}
		}
	}
}

