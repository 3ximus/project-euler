s = ''.join(str(i) for i in range(1,999999))
result = 1
for d in [s[10**i-1] for i in range(7)]:
	result *= int(d)
print(result)

