def get_factors(n):
	upper_bound = n // 3
	lower_bound = 3
	f = 6 # account for n and 1
	while lower_bound < upper_bound:
		if n % lower_bound == 0:
			upper_bound = n // lower_bound
			f += 2
		lower_bound += 1
	return f


t_num = 1 # triangle number
n = 1 # nth triangle number
target = 500
while True:
	if t_num % 10 == 0 and t_num % 7 == 0 and t_num % 3 == 0:
		if get_factors(t_num) > target:
			break
	n += 1
	t_num += n
	if n == 10000000: break
print(t_num)

