p10 = []
for i in range(20): # generate a powers of 10 list to speed up the process
	p10.append(10**i)

def digit_at(x,p): # digit at position p in number x
	return (x % p10[p])//p10[p-1]

def digit_power_sum(n, p):
	size = dsum = 0
	x = p10[0]
	while n // x != 0:
		size += 1
		x = p10[size]
	for i in range(1,size+1):
		dsum += digit_at(n, i)**p
	return dsum

numbers = []
maxNum = 9**5
while maxNum < len(str(maxNum)) * 9**5:
    maxNum = len(str(maxNum)) * 9**5
for n in range(2, maxNum):
	if n == digit_power_sum(n,5):
		numbers.append(n)
print(sum(numbers))