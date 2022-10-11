a = 1; b = 2
s = 0; n = 4000000
while b < n:
	if not b % 2:
		s += b
	c = a + b
	a = b
	b = c
print(s)
