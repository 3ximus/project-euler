from math import factorial

n = 1000000 - 1 # offset this a bit to be correct
digits = set((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
# each digit has factorial(10)/10 = factorial(10-1) = factorial(9) numbers that start with it
# so when ordered the first factorial(9) numbers start with zero, the second factorial(9) numbers start with 1, etc

p10 = []
for i in range(len(digits)): # generate a powers of 10 list to create the number easier
	p10.append(10**i)
number = 0

def find_number(digits, order=0, number=0, c=len(digits) - 1):
	"This function returns the next digit in the number"
	if not digits and order == n: return number, order
	if not digits: return None, None
	fac = factorial(len(digits) - 1)
	for index, i in reversed(list(enumerate(digits))):
		if fac * index + order <= n:  # numbers that would be generated starting with <=i
			digits_copy = digits.copy()
			digits_copy.remove(i)
			new_number, new_order = find_number(digits_copy, order + fac * index, number + p10[c] * i, c - 1)
			if new_order == n: return new_number, new_order


number, order = find_number(digits)
print(number)


