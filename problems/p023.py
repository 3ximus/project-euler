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

counter = 0
for i in range(1, n + 1):
	is_sum_of_abundants = False
	for j in abundants:
		if (i - j) in abundants:
			is_sum_of_abundants = True # can be written as sum of 2 abundants
			break
	if not is_sum_of_abundants:
		counter += i
print(counter)
