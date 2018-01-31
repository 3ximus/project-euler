primes = set()

def is_prime(n):
	if n in primes: return True # speedup
	for i in range(2, int(n**0.5 + 1)):
		if n % i == 0: return False
	primes.add(n)
	return True

def verify(n):
	if not is_prime(n): return False
	ns = str(n)
	# only check usefull permutations, ignore single digits
	for i in range(1, len(ns) - 1):
		if not is_prime(int(ns[i:])): return False
	for i in range(2, len(ns)):
		if not is_prime(int(ns[:i])): return False
	return True

def product_permutations(*args, repeat=1):
	# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
	pools = [tuple(pool) for pool in args] * repeat
	result = [[]]
	for pool in pools:
		result = [x + [y] for x in result for y in pool]
	for prod in result:
		yield ''.join(prod)

def generate_valid_numbers():
	allowed = ['2357', '379', '37'] # first, middle and last digits of ever allowed number
	for i in allowed[0]:
		for j in allowed[-1]:
			yield int(i+j)
	size = 1
	while True:
		for i in allowed[0]:
			for j in allowed[-1]:
				for x in product_permutations(allowed[1], repeat=size):
					yield int(i+x+j)
		size += 1

count = 0
sumation = 0
for i in generate_valid_numbers():
	if verify(i):
		count += 1
		print(count, i)
		sumation += i
	if count == 11:
		break
print(sumation)
