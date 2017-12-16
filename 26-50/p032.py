min_product = 1234
max_product = 9876

set_total = set('123456789')

def variacoes(conj_segunda_geracao, prev=''):
	if len(conj_segunda_geracao) == 1:
		yield prev + conj_segunda_geracao.pop()
	for c in conj_segunda_geracao:
		yield from variacoes(conj_segunda_geracao - set(c), prev + c)

def aprova_multiplicacoes(produto, conj_multiplicadores):
	# 1 * 4
	for d in conj_multiplicadores:
		for v in variacoes(conj_multiplicadores - set(d)):
			if int(d) * int(v) == produto:
				return True
	# 2 * 3
	for d in conj_multiplicadores:
		for e in conj_multiplicadores - set(d):
			for v in variacoes(conj_multiplicadores - set(d + e)):
				if int(d + e) * int(v) == produto:
					return True
	return False


soma = 0
for i in range(min_product, max_product + 1):
	if not '0' in str(i) and len(set(str(i))) == 4:
		if aprova_multiplicacoes(i, set_total - set(str(i))):
			soma = soma + i

print(soma)
