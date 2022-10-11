target = 1000

p10 = []
for i in range(4): # generate a powers of 10 list to speed up the process
	p10.append(10**i)

def digit_at(x,p): # digit at position p in number x
	return (x % p10[p])//p10[p-1]

t = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # starts at 1
d = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
thousand = 8

s = 0
for i in range(20): s += t[i]
for i in range(20, 100): s+= d[digit_at(i,2)] + t[digit_at(i, 1)]
for i in range(100, target):
	if i % 100 == 0: s += t[digit_at(i,3)] + hundred
	else:
		if i % 100 < 20: s += t[digit_at(i,3)] + hundred + 3 + t[i%100]
		else: s += t[digit_at(i,3)] + hundred + 3 + d[digit_at(i,2)] + t[digit_at(i, 1)]
print(s+len('onethousand'))
