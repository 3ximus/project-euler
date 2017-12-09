p10 = []
for i in range(8): # generate a powers of 10 list to speed up the process
	p10.append(10**i)

def digit_at(x,p): # digit at position p in number x
	return (x % p10[p])//p10[p-1]

def is_palindrome(x):
	size = 0
# 6 is the max size of the product of 2 three digit numbers (7 is just to be safe)
	for y in range(0,7):
		if x//p10[y] == 0: break
		size += 1
	l = size
	for r in range( 1,7):
		if r >= size: return True
		elif not digit_at(x,r) == digit_at(x,l): return False
		l -= 1

max_palindrome = 0
for n1 in range(999, 100, -1):
	for n2 in range(n1,100,-1):
		m = n1*n2
		if is_palindrome(m) and max_palindrome < m:
			max_palindrome = m
print(max_palindrome)




