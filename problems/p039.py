"""TODO Should be optimised"""

p_max = 1000

def get_solutions(number):
	solutions = 0
	for i in range(1, int(number/3)):
		for j in range(i, i + int(number/3)):
			if (number - i - j)**2 == i**2 + j**2:
				solutions += 1
	return solutions

max_solutions = 0
number = 0

for i in range(p_max, 1, -1):
	s = get_solutions(i)
	if s > max_solutions:
		max_solutions = s
		number = i
		print(i, max_solutions)

