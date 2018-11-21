from itertools import permutations

primes = (2, 3, 5, 7 , 11, 13, 17)
def is_valid(number):
	for c in range(7,0,-1):
		if int(number[c:c+3]) % primes[c - 1] != 0:
			return False
	return True

print(sum([int(''.join(i)) for i in permutations('0123456789') if is_valid(''.join(i))]))
