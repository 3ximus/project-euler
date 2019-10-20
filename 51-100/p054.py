def to_number(card):
	if card[0] in 'TJQKA':
		return 10 + list('TJQKA').index(card[0])
	else:
		return int(card[0])

# =========================================

def same_suit(hand):
	return all((card[1]==hand[0][1] for card in hand[0:])) 

def verify_same_symbol(hand, amount):
	hand_in_symbols = [card[0] for card in hand]
	cards_to_verify = 6 - amount
	return any((hand_in_symbols.count(hand_in_symbols[card]) == amount for card in range(cards_to_verify)))

def which_same_symbol(hand, amount):
	hand_in_symbols = [card[0] for card in hand]
	cards_to_verify = 6 - amount
	for card in range(cards_to_verify):
		if hand_in_symbols.count(hand_in_symbols[card]) == amount:
			return hand_in_symbols[card]

def which_same_symbol_2pairs(hand):
	hand_in_symbols = [card[0] for card in hand]
	pair_cards = set()
	for card in range(4):
		if hand_in_symbols.count(hand_in_symbols[card]) == 2:
			pair_cards.add(hand_in_symbols[card])
	return pair_cards

def straight(hand):
	hand_in_numbers = [to_number(card) for card in hand]
	min_card = min(hand_in_numbers)
	return all((number in hand_in_numbers for number in range(min_card+1, min_card+5)))

# =========================================

def rf(hand):
	return same_suit(hand) and all((any(symbol in card for symbol in 'TJQKA') for card in hand))

def sf(hand):
	return same_suit(hand) and straight(hand)

def foak(hand):
	return verify_same_symbol(hand, 4)

def fh(hand):
	return verify_same_symbol(hand, 3) and verify_same_symbol(hand, 2)

def toak(hand):
	return verify_same_symbol(hand, 3)

def tp(hand):
	hand_in_symbols = [card[0] for card in hand]
	repeated_cards = 0
	for card in range(4):
		if hand_in_symbols.count(hand_in_symbols[card]) == 2:
			repeated_cards += 1
			if repeated_cards == 3:
				return True
	return False

def op(hand):
	return verify_same_symbol(hand, 2)

# ========================================

def foak_untie(hand1, hand2):
	return to_number(which_same_symbol(hand1, 4)) > to_number(which_same_symbol(hand2, 4))

def fh_untie(hand1, hand2):
	return toak_untie(hand1, hand2)

def toak_untie(hand1, hand2):
	return to_number(which_same_symbol(hand1, 3)) > to_number(which_same_symbol(hand2, 3))

def tp_untie(hand1, hand2):
	h1_pairs = which_same_symbol_2pairs(hand1)
	h2_pairs = which_same_symbol_2pairs(hand2)

	if max([to_number(card) for card in h1_pairs]) > max([to_number(card) for card in h2_pairs]):
		return True
	elif min([to_number(card) for card in h1_pairs]) > min([to_number(card) for card in h2_pairs]):
		return True
	else:
		for card in hand1:
			for pair_card in h1_pairs:
				if pair_card not in card:
					h1_non_paired = card
		for card in hand2:
			for pair_card in h2_pairs:
				if pair_card not in card:
					h2_non_paired = card
		return to_number(h1_non_paired) > to_number(h2_non_paired)

def op_untie(hand1, hand2):
	if to_number(which_same_symbol(hand1, 2)) > to_number(which_same_symbol(hand2, 2)):
		return True
	elif to_number(which_same_symbol(hand1, 2)) == to_number(which_same_symbol(hand2, 2)): 
		pair_symbol = which_same_symbol(hand1, 2)
		hand1 = [card for card in hand1 if pair_symbol not in card]
		hand2 = [card for card in hand2 if pair_symbol not in card]
		return highest_card_untie(hand1, hand2)
	return False

def highest_card_untie(hand1, hand2):
	return max([to_number(card) for card in hand1]) > max([to_number(card) for card in hand2])


# ========================================

def rank(hand):
	methods = [rf, sf, foak, fh, same_suit, straight, toak, tp, op]
	for rank, method in enumerate(methods):
		if method(hand):
			return rank
	return len(methods)

# =========================================

with open('p054.txt', 'r') as fp:
	p1_hands = 0
	untie_ranks = [None, None, foak_untie, fh_untie, highest_card_untie, highest_card_untie, toak_untie, tp_untie, op_untie, highest_card_untie]
	for line in fp:
		line = line.strip('\n').split()
		p1, p2 = line[:5], line[5:]
		r1, r2 = rank(p1), rank(p2)
		if r1 < r2:
			p1_hands += 1
		if r1 == r2:
			if untie_ranks[r1](p1, p2):
				p1_hands += 1
	print(p1_hands)





