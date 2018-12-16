with open('51-100/p081.txt', 'r') as fp: mat = [[int(x) for x in line.split(',')] for line in fp]

def down(i, j, cost): return i+1, j, cost+mat[i+1][j]
def right(i, j, cost): return i, j+1, cost+mat[i][j+1]
def neighbours(i, j, cost):
	ret = []
	if i < 79: ret.append(down(i, j, cost))
	if j < 79: ret.append(right(i, j, cost))
	return ret

def min_unvisited():
	key, m = (0,0), 2**32
	for k in unvisited:
		if unvisited[k] < m:
			key = k
			m = unvisited[k]
	return key

# initialize all unvisited with 2**32
unvisited = dict(zip([(i,j) for i in range(80) for j in range(80)], [2**32 for k in range(80*80)]))
unvisited[(0,0)] = mat[0][0]
i, j, cost = 0, 0, mat[0][0]
while i != 79 or j != 79:
	for x in neighbours(i, j, cost):
		if x[:2] in unvisited and unvisited[x[:2]] > x[2]:
			unvisited[x[:2]] = x[2]
	del(unvisited[(i,j)])
	i, j = min_unvisited()
	cost = unvisited[(i,j)]
print(cost)