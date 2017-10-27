def is_prime(n):
	for i in range(2,int(n**0.5+1)):
		if n % i == 0:
			return False
	return True

c = 2
nth = 0
target = 10001
while nth != target:
	if is_prime(c):
		nth += 1
	c += 1
print(c-1)
