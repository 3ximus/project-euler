bound = 1000
from lib.eratosthenes import sieve
primes = set(sieve(100000))
is_prime = lambda x: x in primes

def quadratic(n, a, b):
	return n * n + a * n + b

def test_quadratic(a,b):
	n = 0
	while True:
		if is_prime(abs(quadratic(n, a, b))): n += 1
		else: break
	return n

primes = set(filter(is_prime, range(0, bound)))
max_primes = 0
max_primes_mul = 0
for i in primes:
	for j in primes:
		counter = max(test_quadratic(i, j), test_quadratic(-i, -j),
					  test_quadratic(-i, j), test_quadratic(i, -j))
		if counter > max_primes:
			max_primes = counter
			max_primes_mul = i*j
print(max_primes_mul) # NOTE, test this with a - sign since one of i or j might be negative, and makes the code easier
