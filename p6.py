n = 100
sq_sum = 0
s = 0
for i in range(n+1):
	sq_sum += i**2
	s += i
print(s**2 - sq_sum)
