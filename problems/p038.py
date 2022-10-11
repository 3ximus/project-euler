
def only_unique_digits(number_string):
	seen = set()
	for c in number_string:
		if c in seen: return False
		seen.add(c)
	return True

def gen_next_integer():
	integer = 8
	while True:
		integer += 1
		integer_string = str(integer)
		if integer_string.startswith('9') and only_unique_digits(str(integer)):
			yield integer, integer_string
		if integer_string.startswith('1'):
			integer += 8 * 10 ** (len(integer_string) - 1) # skip until the next number starting with 9
		if len(integer_string) > 5:
			break

for integer, integer_string in gen_next_integer():
	concat = integer_string
	for i in range(2,7):
		integer_string += str(integer * i)
		if len(integer_string) == 9 and '0' not in integer_string and only_unique_digits(integer_string):
				print(integer_string, integer)

