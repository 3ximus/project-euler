triangle = []
fd = open('p067.txt','r')
for line in fd:
	triangle.append([int(x) for x in line.split()])
fd.close()

cache = {}
levels = len(triangle)

def get_path(i,j, path = 0):
	if i == levels: return path
	path += triangle[i][j]
	if (i,j) in cache: return cache[(i,j)]
	t = max(get_path(i+1,j, path), get_path(i+1,j+1, path))
	cache[(i,j)] = t
	return t

print(get_path(0,0))
