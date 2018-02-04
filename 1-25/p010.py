from lib.eratosthenes import ESieve

target = 2000000
sieve = ESieve().initialize(target)
print(sum(sieve.primes))
