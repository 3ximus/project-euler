def how_many_fit(small_side, big_side):
	# how many small sides fit on one big size
	return big_side - small_side + 1

def how_many_squares(w, h):
	c = 0
	for i in range(1, w+1):
		for j in range(1, h+1):
			c += how_many_fit(i, w) * how_many_fit(j, h)
	return c

erro = 100
for i in range(100):
	for j in range(100):
		x = how_many_squares(i,j)
		if abs(x - 2000000) < erro:
			erro = x - 2000000
			print("Area", i*j, "n_squares_difference", erro)

