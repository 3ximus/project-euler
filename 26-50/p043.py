from itertools import permutations

sumation = 0
primes = (2, 3, 5, 7 , 11, 13, 17)
for i in permutations('0123456789'):
	number = ''.join(i)
	failed = False
	for c in range(1,8):
		if int(number[c:c+3]) % primes[c - 1] != 0:
			failed = True
			break
	if not failed: sumation += int(number)
print(sumation)
