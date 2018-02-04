from lib.eratosthenes import ESieve

target = 2000000
print(sum(ESieve(target).sieve()))
