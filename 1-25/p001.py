n = 1000
s = 0
x = 0
while x < n:
	if (not x % 3) or (not x % 5): s +=x
	x += 1
print(s)
