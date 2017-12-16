target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
cache = {}

def sum_coins(index, n):
	if n == 0:
		return 1
	if n < 0:
		return 0
	if index <= 0 and n >= 1:
		return 0

	# NOTE without cache we just needed to run this:
	# return sum_coins(index - 1, n) + sum_coins(index, n - coins[index - 1])
	# the rest of the code makes use of the cache

	val = (index - 1, n)
	if not val in cache:
		a = sum_coins(index - 1, n)
		cache[val] = a
	else:
		a = cache[val]

	val = (index, n - coins[index - 1])
	if not val in cache:
		b = sum_coins(index, n - coins[index - 1])
		cache[val] = b
	else:
		b = cache[val]
	return a + b

print(sum_coins(len(coins), target))


