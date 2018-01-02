primes = set()

def is_prime(n):
	#if n in primes: return True # speedup
	for i in range(2, int(n**0.5 + 1)):
		if n % i == 0: return False
	#primes.add(n)
	return True

def get_truncation(n):
	ns = str(n)
	for i in range(1, len(ns)):  # left to right
		yield int(ns[:i])
		yield int(ns[i:])

# NOTE this is not really god enough, lets try and generate new
def product_permutations(*args, repeat=1):
	# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
	pools = [tuple(pool) for pool in args] * repeat
	result = [[]]
	for pool in pools:
		result = [x + [y] for x in result for y in pool]
	for prod in result:
		yield int(''.join(prod))

allowed_digits = '375'
count = 0
sumation = 0
k = 0
while count != 14: # its not 11 to account for 3, 5 and 7 that should be counted aswell
	k += 1
	for i in product_permutations(allowed_digits, repeat=k):
		if is_prime(i) and all([is_prime(x) for x in get_truncation(i)]):
			count += 1
			print("C: ", i)
			sumation += i
print(sumation)


