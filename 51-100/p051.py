from lib.eratosthenes import sieve
primes_list = sieve(999999)[5781:]
primes = set(primes_list)
is_prime = lambda x: x in primes

def replace(string, replacement, *pos):
	new, i = '', 0
	for p in pos:
		new += string[i:p] + replacement
		i = p+1
	return new + string[i:]

def generate_family(n, digit):
	return [replace(n, str(x), *[x for x in range(len(n)) if n[x] == digit]) for x in (range(10) if n[0] != digit else range(1,10))]

def is_8family(family):
	return sum(1 for x in family if is_prime(int(x))) == 8

def search():
	for dig in '012':
		for number in (d for d in primes_list if dig in str(d)[:-1]):
			if is_8family(generate_family(str(number), dig)):
				return number
print(search())