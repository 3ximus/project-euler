def is_prime(n):
	if n in primes: return True # speedup
	for i in range(2,int(n**0.5+1)):
		if n % i == 0: return False
	return True

def get_truncation(n):
	ns = str(n)
	for i in range(1, len(ns)): # left to right
		yield int(ns[:i])

forbidden_digits = set('1234567890') - set('1379')
primes = set()
count = 0
sumation = 0
i = 8
while count != 11:
	if any([x in str(i) for x in forbidden_digits]): # sleeve trick xD
		continue
	if is_prime(i) and all([is_prime(x) for x in get_truncation(i)]):
		primes.add(i)
		primes |= set(get_truncation(i))
		count += 1
		sumation += i
	i += 1

print(sumation)

