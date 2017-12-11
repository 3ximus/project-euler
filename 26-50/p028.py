n = 1001

def yield_them_values(start,step):
	value = start
	for _ in range(4): # neat, this ignores the loop variavel
		value += step
		yield value

side = 2
start = 1
diag_sum = 1
while side < 1001: # last iteration should be when side=1000
	for x in yield_them_values(start, side):
		diag_sum += x
	start = x
	side += 2

print(diag_sum)

