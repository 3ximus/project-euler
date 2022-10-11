target = 20
cache = {}
def paths(i, j):
	if i == target and j == target: return 1
	if (i,j) in cache: return cache[(i,j)]
	c = 0
	if i == target and j != target:
		c = paths(i, j+1)
	elif i != target and j == target:
		c = paths(i+1, j)
	else:
		c = paths(i, j+1) + paths(i+1, j)
	cache[(i,j)] = c
	return c
print(paths(0,0))

