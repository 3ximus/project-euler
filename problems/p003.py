
def is_prime(n):
	for i in range(2,int(n**0.5+1)):
		if n % i == 0:
			return False
	return True

n = 600851475143
maxbound = n
minbound = 2
prime = 0
while minbound <= maxbound:
	d = n % minbound
	maxbound = n // minbound
	if d == 0:
		if is_prime(maxbound):
			prime = maxbound
			break
		if is_prime(minbound):
			prime = minbound
	minbound += 1
print(prime)





