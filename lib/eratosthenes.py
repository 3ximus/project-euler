# Sieve of Eratosthenes for prime numbers

class ESieve:
	def __init__(self, max_prime):
		self.max_prime = max_prime
		self.primality_list = [True] * max_prime
		self.primality_list[0] = self.primality_list[1] = False

