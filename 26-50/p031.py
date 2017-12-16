n = 4
coins = [1, 2, 3, 10, 20, 50, 100, 200]

total_coins = len(coins)
def coin_value(ci=0, value=0, combinations=0):
	if value == n:
		return combinations + 1
	if ci == total_coins or value > n:
		return combinations
	for i in range(n // coins[ci]):
		combinations = coin_value(ci + 1, value + i * coins[ci], combinations)
	return combinations

print(coin_value())


