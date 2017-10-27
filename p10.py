def is_prime(n):
	for i in range(2,int(n**0.5+1)):
		if n % i == 0:
			return False
	return True

s = 5 # skip 2 and 3 in order to skip all even numbers on iteration
target = 2000000
for i in range(5, target, 2):
	if is_prime(i):
		s += i
print(s)
