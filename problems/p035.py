from lib.eratosthenes import sieve
primes = set(sieve(1000000))
is_prime = lambda x: x in primes
get_rotation = lambda n: (int(n[i:] + n[:i]) for i in range(1, len(n))) # return generator containing all string rotations
print(len([i for i in range(101, 1000000, 2) if is_prime(i) and all((is_prime(x) for x in get_rotation(str(i))))]) + 13)

