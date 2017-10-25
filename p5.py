d = 2520 # starting value
stop = False
while not stop:
	stop = True # flag the success
	for i in range(20,10,-1): # the unique divisors
		if d % i:
			stop = False
			break
	d += 20
print(d-20)

