// vim: foldmethod=marker
package lib

import "math"

func EratosthenesSieve(n int) []int {
	return thirds(n);
}

func sum(array []int) int { // {{{
	result := 0
	for _, v := range array {
		result += v
	}
	return result
} // }}}

func basic(n int) []int { // {{{
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
} // }}}

func halved(n int) []int { // {{{
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
} // }}}

func thirds(n int) []int { // {{{
	size := int(math.Ceil(float64(n)/3));
	if n % 6 == 2 {
		size += 1;
	}
	marks := make([]bool, size);
	primes := make([]int, size+1)
	pi := 1

	if n <=1 {
		return make([]int, 0);
	} else if n == 2 {
		return []int{2};
	}

	for i := 3; i <= int(math.Sqrt(float64(n))); i+=3 {
		if !marks[i/3] {
			x := (i + 1) | 1;
			for m := x*x/3; m <= n/3; m += 2*x {
				marks[m] = true
			}
			for m := x*(x-2*(i & 1) +4)/3; m <= n/3; m += 2*x {
				marks[m] = true
			}
		}
	}

	for i := 0; (3 * i + 1) | 1 <= n ; i++ {
		if !marks[i] {
			primes[pi] = (3 * i + 1) | 1;
			pi++;
		}
	}

	primes[1] = 3;
	primes[0] = 2
	return primes[:pi];
} // }}}

// func main() {
// 	target := 20000000;
// 	start := time.Now();
// 	fmt.Printf("Sieve Basic %v\n %v\n", sum(basic(target)), time.Since(start));
// 	start = time.Now();
// 	fmt.Printf("Sieve Half  %v\n %v\n", sum(halved(target)), time.Since(start));
// 	start = time.Now();
// 	fmt.Printf("Sieve Third %v\n %v\n", sum(thirds(target)), time.Since(start));
// }
