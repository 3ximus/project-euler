from fractions import Fraction
lower_bound = 11
higher_bound = 99

num_prod = 1
den_prod = 1
for denominator in [x for x in range(lower_bound, higher_bound) if not '0' in str(x)]:
	for numerator in [i for i in range(lower_bound, denominator) if any([x in str(i) for x in str(denominator)]) and '0' not in str(i)]:
		new_denominator = int(str(denominator)[abs([x in str(numerator) for x in str(denominator)].index(True) - 1)])
		new_numerator = int(str(numerator)[abs([x in str(denominator) for x in str(numerator)].index(True) - 1)])
		if numerator / denominator == new_numerator / new_denominator:
			num_prod *= numerator
			den_prod *= denominator

print(Fraction(num_prod, den_prod).denominator)