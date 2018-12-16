import decimal

decimal.getcontext().prec = 102 # desirable precision
s = 0
p = pow(10, 99)
for z in range(2, 100):
	q = decimal.Decimal(z).sqrt()
	s += sum(int(c) for c in str(q * p)[:100]) if q % 1 != 0 else 0
print(s)
