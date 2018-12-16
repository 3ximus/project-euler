import heapq
with open('51-100/p081.txt', 'r') as fp: mat = [[int(x) for x in line.split(',')] for line in fp]

def down(i, j, cost): return i+1, j, cost+mat[i+1][j]
def right(i, j, cost): return i, j+1, cost+mat[i][j+1]
def left(i, j, cost): return i, j-1, cost+mat[i][j-1]
def up(i, j, cost): return i-1, j, cost+mat[i-1][j]
def neighbours(i, j, cost):
	ret = []
	if i > 0: ret.append(up(i,j,cost))
	if j > 0: ret.append(left(i,j,cost))
	if i < 79: ret.append(down(i, j, cost))
	if j < 79: ret.append(right(i, j, cost))
	return ret

def min_unvisited(unvisited):
	key, m = (0,0), 2**32
	for k in unvisited:
		if unvisited[k] < m:
			key = k
			m = unvisited[k]
	return key

def min_path(initial, targets):
	# initialize all unvisited with 2**32
	unvisited = dict(zip([(i,j) for i in range(80) for j in range(80)], [2**32 for k in range(80*80)]))
	unvisited[(0,0)] = mat[0][0]
	hq = [] # heap queue
	i, j = initial
	cost = mat[i][j]
	while i != targets[0] or j != targets[1]:
		for x in neighbours(i, j, cost):
			if x[:2] in unvisited and unvisited[x[:2]] > x[2]:
				heapq.heappush(hq, (x[2], x[:2]))
				unvisited[x[:2]] = x[2]
		del(unvisited[(i,j)])
		cost, ij = heapq.heappop(hq)
		i, j = ij
	return cost

print(min_path((0,0), (79,79)))