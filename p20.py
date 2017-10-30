from math import factorial
p10 = [1]
n = factorial(100)
size = 0
x = 10**size
while n // x != 0:
	size += 1
	x = 10**size
	p10.append(x)

def digit_at(x,p): # digit at position p in number x
	return (x % p10[p])//p10[p-1]

s = 0
for a in range(1, size+1):
	s += digit_at(n, a)
print(s)
