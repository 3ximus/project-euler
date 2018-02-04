# Sieve of Eratosthenes for prime numbers

from time import time

class ESieve:
	def __init__(self, max_number):
		# this wheel has the the steps to avoid all multiples of 2, 3, 5 and 7, avoiding 77% of all composites
		self._wheel = [2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4,
					2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 10, 2, 10]
		self._wheel_size = len(self._wheel)
		self.max_number = max_number

	def init_static(self):
		'''Create list of primes until max_number'''
		_ptable = [True] * self.max_number
		_ptable[0] = _ptable[1] = False
		primes = []
		limit = int(self.max_number ** 0.5) + 1
		for i in range(limit):
			if _ptable[i]:
				for x in range(i ** 2, self.max_number, i):
					_ptable[x] = False
				primes.append(i)
		for i in range(limit, self.max_number):
			if _ptable[i]:
				primes.append(i)
		return primes

	def spin_wheel(self): # TODO broken
		value = 13
		n = 1
		while value < self.max_number:
			yield value
			value += self._wheel[n % self._wheel_size]
			n += 1

	def generate(self):
		'''Generator for prime numbers until max_number'''
		yield 2; yield 3; yield 5; yield 7; yield 11; yield 13
		ps = self.generate() # yay recursion
		p = ps.__next__() and ps.__next__()
		q = p**2
		sieve = {}
		n = 13
		while True:
			if n > self.max_number:
				break
			if n not in sieve:
				if n < q:
					yield n
				else:
					inext = q + 2 * p
					step = 2 * p
					while inext in sieve:
						inext += step
					sieve[inext] = step
					p = ps.__next__()
					q = p**2
			else:
				step = sieve.pop(n)
				inext = n + step
				while inext in sieve:
					inext += step
				sieve[inext] = step
			n += 2
			# n += self.spin_wheel().__next__()

if __name__ == '__main__':
	# project euler 10 example
	target = 2000000

	ts = time()
	print(sum(ESieve(target).init_static()))
	print("  ", time() - ts)

	ts = time()
	print(sum(ESieve(target).generate()))
	print("  ", time() - ts)
