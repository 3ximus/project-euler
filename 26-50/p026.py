p10 = []
for i in range(20): # generate a powers of 10 list
	p10.append(10**i)
pminus10 = []
for i in range(20): # generate a negative powers of 10 list
	pminus10.append(10**-i)

def digit_at(x,p,n=1): # digit at position p in number x, n is the amount of digits returned (backwards)
	return int((x / pminus10[p]) % p10[n])


