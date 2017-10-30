triangle = []
fd = open('p067.txt','r')
for line in fd:
	triangle.append([int(x) for x in line.split()])
fd.close()

cache = {}
levels = len(triangle)

def get_path(i,j):
	if i == levels-1: return triangle[i][j]
	if (i,j) in cache: return cache[(i,j)]
	cache[(i,j)] = max(triangle[i][j] + get_path(i+1,j), triangle[i][j] + get_path(i+1,j+1))
	return cache[(i,j)]

print(get_path(0,0))
