def find_cycle(d):
	rlist = []
	qlist_len = 0
	remainder = 1
	while remainder:
		remainder = remainder % d # allows to generate infinited decimal numbers
		if remainder in rlist:
			return qlist_len - rlist.index(remainder)
		rlist.append(remainder)
		remainder *= 10
		qlist_len+=1
	return 0

d = 1000
many_digits = 0
max_d = 0
for n in range(2, d):
	val = find_cycle(n)
	if  val > many_digits:
		many_digits = val
		max_d = n
print(max_d)
