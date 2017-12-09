n = 28123

def is_abundant(n):
	upper_bound = n
	lower_bound = 1
	f = -n # do not count n itself
	while lower_bound < upper_bound:
		if n % lower_bound == 0:
			upper_bound = n // lower_bound
			f += (upper_bound + lower_bound) if upper_bound != lower_bound else upper_bound
			if f > n : return True
		lower_bound += 1
	return False

abundants = set()
for i in range(2, n + 1):
	if is_abundant(i):
		abundants.add(i)

non_abundants = 0
for i in range(1, n + 1):
	if i not in abundants:
		for j in abundants:
			if (i - j) not in abundants:
				non_abundants += i
				break
print(non_abundants)
