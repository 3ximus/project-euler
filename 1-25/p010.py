from lib.eratosthenes import ESieve

s = 0
target = 2000000
sieve = ESieve().initialize(target)
for i,is_prime in enumerate(sieve.primes):
	if is_prime: s += i
print(s)
