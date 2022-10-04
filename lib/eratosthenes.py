''' Eratosthenes sieve based to generate prime numbers list

Multiple methods are implemented, to use the fastest one use sieve()

Improvements based on this: https://codereview.stackexchange.com/a/42439'''


import numpy

def sieve(max_number):
	'''Fastest sieve form'''
	return sieve_numpy_3(max_number)

def sieve_simple(max_number):
	'''Slowest and simplest form of the sieving algorithm'''
	_ptable = [True] * max_number
	for i in range(3, int(max_number ** .5) + 1, 2):
		if _ptable[i]:
			for x in range(i ** 2, max_number, 2 * i):
				_ptable[x] = False
	return [2] + [p for p in range(3, max_number , 2) if _ptable[p]]

def sieve_slice(max_number):
	'''Improved form of the sieving algorithm using slice assignment'''
	_ptable = [True] * max_number
	for i in range(3, int(max_number ** .5) + 1, 2):
		if _ptable[i]:
			# this calculates size of the slice len(_ptable[i*i::2*i]) in a quicker way and assigns False to it! clever!
			_ptable[i*i::2*i] = [False] * ((max_number - i*i - 1) // (2*i) + 1)
	return [2] + [p for p in range(3, max_number , 2) if _ptable[p]]

def sieve_numpy(max_number):
	'''Faster form using numpy arrays'''
	_ptable = numpy.ones(max_number, dtype=bool)
	_ptable[:2] = False
	_ptable[4::2] = False
	for i in range(3, int(max_number ** .5) + 1, 2):
		if _ptable[i]:
			_ptable[i*i::2*i] = False
	return _ptable.nonzero()[0] # grab nonzero indexes

def sieve_numpy_2(max_number):
	'''Faster form using numpy arrays with half the space'''
	_ptable = numpy.ones(max_number // 2, dtype=bool)
	for i in range(3, int(max_number ** .5 ) + 1, 2):
		if _ptable[i // 2]:
			_ptable[i*i//2::i] = False
	result = 2 * _ptable.nonzero()[0] + 1
	result[0] = 2
	return result

def sieve_numpy_3(max_number):
	'''Fastest form using numpy arrays with a third of the space'''
	# use (max_number % 6 == 2) to fix size
	_ptable = numpy.ones(max_number//3 + (max_number % 6 == 2), dtype=bool)
	for i in range(3, int(max_number ** .5 ) + 1, 3):
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
	target = 20000000

	ts = time()
	print("Simple ", sum(sieve_simple(target)))
	print("  ", time() - ts)

	ts = time()
	print("Slice ", sum(sieve_slice(target)))
	print("  ", time() - ts)

	ts = time()
	print("Numpy ", sum(sieve_numpy(target)))
	print("  ", time() - ts)

	ts = time()
	print("Numpy2 ", sum(sieve_numpy_2(target)))
	print("  ", time() - ts)

	ts = time()
	print("Numpy3 ", sum(sieve_numpy_3(target)))
	print("  ", time() - ts)
