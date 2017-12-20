def is_palindrome(x):
	x = str(x)
	return x == x[::-1]

print(sum([i for i in range(1000000) if is_palindrome(i) and is_palindrome(bin(i)[2:])])) # one line... beautifull...