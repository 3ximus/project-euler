target = 1000000
cache = {} # should be enough

def collatz(n):
	if n == 1: return 1
	if n in cache: return cache[n]
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
print(starting_n, m_chain)


