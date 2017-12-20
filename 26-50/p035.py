
def is_prime(n):
	for i in range(2,int(n**0.5+1)):
		if n % i == 0: return False
	return True

def get_rotation(n):
	ns = str(n)
	for i in range(1, len(ns)):
		yield int(ns[i:] + ns[:i])

forbidden_digits = set('1234567890') - set('1379')
primes = set()
for i in range(101, 1000000, 2):
	if i in primes or any([x in str(i) for x in forbidden_digits]): # sleeve trick xD
		continue
	if is_prime(i) and all([is_prime(x) for x in get_rotation(i)]):
		primes.add(i)
		primes |= set(get_rotation(i))

print(len(primes) + 13)

