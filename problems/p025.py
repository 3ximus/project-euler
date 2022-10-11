n = 1000
fib = [1, 1, 2, 3, 5]
size = len(fib)
p10 = 10**(n-1)

fib_ind = 0
index = size+1
while True:
	fib[fib_ind] = fib[fib_ind-1] + fib[fib_ind-2]
	fib_ind = (fib_ind + 1) % size # length of fib
	if fib[fib_ind-1] > p10:
		print(index)
		break
	index+=1


