# Sieve of Eratosthenes for prime numbers

import numpy

class ESieve:
	''' Eratosthenes sieve based to generate prime numbers list

	Multiple methods are implemented, to use the fastest one use sieve()

	Improvements based on this: https://codereview.stackexchange.com/a/42439'''

	def __init__(self, max_number):
		# this wheel has the the steps to avoid all multiples of 2, 3, 5 and 7, avoiding 77% of all composites
		self.max_number = max_number

	def sieve(self):
		'''Fastest sieve form'''
		return self.sieve_numpy_3()

	def sieve_simple(self):
		'''Slowest and simplest form of the sieving algorithm'''
		_ptable = [True] * self.max_number
		for i in range(3, int(self.max_number ** .5) + 1, 2):
			if _ptable[i]:
				for x in range(i ** 2, self.max_number, 2 * i):
					_ptable[x] = False
		return [2] + [p for p in range(3, self.max_number , 2) if _ptable[p]]

	def sieve_slice(self):
		'''Improved form of the sieving algorithm using slice assignment'''
		_ptable = [True] * self.max_number
		for i in range(3, int(self.max_number ** .5) + 1, 2):
			if _ptable[i]:
				# this calculates size of the slice len(_ptable[i*i::2*i]) in a quicker way and assigns False to it! clever!
				_ptable[i*i::2*i] = [False] * ((self.max_number - i*i - 1) // (2*i) + 1)
		return [2] + [p for p in range(3, self.max_number , 2) if _ptable[p]]

	def sieve_numpy(self):
		'''Faster form using numpy arrays'''
		_ptable = numpy.ones(self.max_number, dtype=bool)
		_ptable[:2] = False
		_ptable[4::2] = False
		for i in range(3, int(self.max_number ** .5) + 1, 2):
			if _ptable[i]:
				_ptable[i*i::2*i] = False
		return _ptable.nonzero()[0] # grab nonzero indexes

	def sieve_numpy_2(self):
		'''Faster form using numpy arrays with half the space'''
		_ptable = numpy.ones(self.max_number // 2, dtype=bool)
		for i in range(3, int(self.max_number ** .5 ) + 1, 2):
			if _ptable[i // 2]:
				_ptable[i*i//2::i] = False
		result = 2 * _ptable.nonzero()[0] + 1
		result[0] = 2
		return result

	def sieve_numpy_3(self):
		'''Fastest form using numpy arrays with a third of the space'''
		# use (self.max_number % 6 == 2) to fix size
		_ptable = numpy.ones(self.max_number//3 + (self.max_number % 6 == 2), dtype=numpy.bool)
		for i in range(3, int(self.max_number ** .5 ) + 1, 3):
			if _ptable[i // 3]:
				p = (i + 1) | 1
				_ptable[p*p//3::2*p] = False
				_ptable[p*(p-2*(i & 1)+4)//3::2*p] = False
		result = (3 * _ptable.nonzero()[0] + 1) | 1
		result[0] = 3
		return numpy.r_[2,result]


if __name__ == '__main__':
	# project euler 10 example
	from time import time
	target = 2000000

	ts = time()
	print("Simple ", sum(ESieve(target).sieve_simple()))
	print("  ", time() - ts)

	ts = time()
	print("Slice ", sum(ESieve(target).sieve_slice()))
	print("  ", time() - ts)

	ts = time()
	print("Numpy ", sum(ESieve(target).sieve_numpy()))
	print("  ", time() - ts)

	ts = time()
	print("Numpy2 ", sum(ESieve(target).sieve_numpy_2()))
	print("  ", time() - ts)

	ts = time()
	print("Numpy3 ", sum(ESieve(target).sieve_numpy_3()))
	print("  ", time() - ts)
