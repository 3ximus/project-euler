# Sieve of Eratosthenes for prime numbers

class ESieve:
	def __init__(self):
		pass

	def initialize(self, max_number):
		'''Generate a boolean list of numbers until max_number'''
		self.max_number = max_number
		self.primes = [True] * max_number
		self.primes[0] = self.primes[1] = False
		for i in range(int(len(self.primes) ** 0.5)):
			if self.primes[i]:
				for x in range(i * i, self.max_number, i):
					self.primes[x] = False
		return self

if __name__ == '__main__':
	# project euler 10 example
	s = 0
	target = 2000000
	sieve = ESieve().initialize(target)
	for i,is_prime in enumerate(sieve.primes):
		if is_prime: s += i
	print(s)
