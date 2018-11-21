from itertools import permutations

def is_prime(n):
	for i in range(2,int(n**0.5+1)):
		if n % i == 0: return False
	return True

numbers = '987654321'
for x in range(len(numbers)):
	for i in permutations(numbers[x:]):
		if is_prime(int(''.join(i))):
			print(int(''.join(i)))
			exit()

