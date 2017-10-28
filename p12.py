#n_divisors = 500
#step = 1000
import time
ts = time.time()

def get_factors(n):
	f = 6 # account for n and 1
	for i in range(n // 3 - 1, 3, -1):
		if n % i == 0:
			f += 1
	return f


t_num = 1 # triangle number
n = 1 # nth triangle number
m = 0
while True:
	if t_num % 10 == 0 and t_num % 7 == 0 and t_num % 3 == 0:
		f = get_factors(t_num)
		if f >= m:
			print(n, t_num, f, "%s" % (time.time() - ts))
			m = f
	n += 1
	t_num += n
	if n == 10000000: break
print(t_num)

