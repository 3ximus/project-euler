n = 10000

def divisors_sum(n):
	upper_bound = n
	lower_bound = 1
	f = 0
	while lower_bound < upper_bound:
		if n % lower_bound == 0:
			upper_bound = n // lower_bound
			f += (upper_bound + lower_bound) if upper_bound != lower_bound else upper_bound
		lower_bound += 1
	return f - n

saved = []
for i in range(2, n + 1):
	saved.append(divisors_sum(i))
count = 0
s = len(saved)
found_amicable = []
for i, v in enumerate(saved):
	r_i = i + 2 # get actual number
	if v - 2 < s and r_i != v and saved[v - 2] == r_i:
		count += r_i
print(count)



