a_min = b_min = 2
a_max = b_max = 100
n = set()
for a in range(a_min, a_max+1):
	for b in range(b_min, b_max+1):
		n.add(a**b)
print(len(n))
