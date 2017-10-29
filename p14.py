target = 1000000
cache = [None] * (target + 1) # should be enough
cache_size = target

def collatz(n):
	if n == 1: return 1
	try:
		if cache[n]: return cache[n]
	except IndexError:
		cache.extend([None] * (n - cache_size + 1))
		cache_size = n + 1
	if n % 2 == 0: new = collatz(n//2) + 1
	else: new = collatz(3*n +1) + 1
	cache[n] = new
	return new

m_chain = 0
starting_n = 0
for i in range(target,1,-1):
	if m_chain < collatz(i):
		m_chain = collatz(i)
		starting_n = i
print(starting_n)


