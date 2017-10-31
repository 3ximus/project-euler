fd = open('p022.txt', 'r')
names = fd.read().split(',')
names = sorted([name.strip('"') for name in names])
fd.close()

def name_score(n, i):
	tc = 0
	for c in name:
		tc += ord(c) - 64
	return tc * (index +1)

score = 0
for index, name in enumerate(names):
	score += name_score(name, index)
print(score)
