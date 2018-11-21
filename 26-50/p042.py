
triangle_set = [1]
def is_triangle(n):
	k = len(triangle_set) + 1
	while n > triangle_set[-1]:
		triangle_set.append((k * (k +1)) // 2)
		k += 1
	return n == triangle_set[-1] or n in triangle_set

character_map = {chr(k):v+1 for (v,k) in enumerate(range(65,91))}
def word_value(word):
	return sum([character_map[c] for c in word])

with open('26-50/p042.txt', 'r') as fd:
	count = 0
	for word in fd.read().split(','):
		if is_triangle(word_value(word.strip('\"'))):
			count += 1
	print(count)