p_left = set() # still prime taking digits left
p_right = set() # still prime taking digits right

def is_prime(n):
	for i in range(2, int(n**0.5 + 1)):
		if n % i == 0: return False
	return True

def verify_left(n):
	if len(n) == 1:
		return True
	if int(n) not in p_left or not is_prime(int(n)):
		return False
	if verify_left(n[1:]):
		p_left.add(int(n))
		return True
	return False

def verify_right(n):
	if len(n) == 1:
		return True
	if int(n) not in p_right or not is_prime(int(n)):
		return False
	if verify_right(n[:-1]):
		p_right.add(int(n))
		return True
	return False

def verify(n):
	if not is_prime(n): return False
	print(n)
	ns = str(n)
	if len(ns) == 2:
		p_left.add(n)
		p_right.add(n)
		return True
	return verify_left(ns[1:]) and verify_right(ns[:-1])

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

# count = 0
# sumation = 0
# for i in generate_valid_numbers():
# 	if verify(i):
# 		count += 1
# 		print(p_left, p_right)
# 		print(count, i)
# 		sumation += i
# 	if count == 11:
# 		break
# print(sumation)
