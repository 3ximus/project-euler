from math import factorial

fact_table = [factorial(i) for i in range(10)]
upper_limit = fact_table[9] * 7 # this could be tweaked
sumation = 0
num = 3
while True:
	if num == upper_limit:
		break
	if num == sum([fact_table[int(x)] for x in str(num)]):
		sumation += num
	num += 1
print(sumation)
