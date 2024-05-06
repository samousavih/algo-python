"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE Input: Tact Coa

Output: True (permutations: "taco cat", "atco eta", etc.)

"""

def is_pal_perm(input):
	chars = [0] * 128
	i=0
	while i < len(input):
		if input[i] != ' ':
			chars[ord(input[i].lower())]+=1
		i+=1
	even_count=0
	for char_count in chars:
		if char_count % 2 != 0:
			even_count+=1
		if even_count > 1:
			return False
	return True

def test_is_pal_perm():
	assert is_pal_perm("Tact Coa") == True
	assert is_pal_perm("AbABc") == True
	assert is_pal_perm("AbADc") == False
test_is_pal_perm()
