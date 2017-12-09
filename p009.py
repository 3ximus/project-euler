# a <= (n-3) // 3
# b < (n-a) // 2
n = 1000
for a in range(3, (n-3)//3): 
	for b in range(a+1, (n-a-1)//2): 
		c = n - a - b
		if a**2 + b**2 == c**2:
			print(a * b * c)
