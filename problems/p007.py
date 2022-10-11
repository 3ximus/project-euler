from lib.eratosthenes import sieve
primes = set(sieve(200000))
is_prime = lambda x: x in primes

c = 2
nth = 0
target = 10001
while nth != target:
	if is_prime(c):
		nth += 1
	c += 1
print(c-1)
