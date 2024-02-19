"""
Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.
"""


def group_anagrams(input):
	groups = {}
	for s in input:
		sorted_string = str(sorted(s))
		if sorted_string in groups:
			groups[sorted_string].append(s)
		else:
			groups[sorted_string] = [s]
	i = 0
	for g in groups:
		for s in groups[g]:
			input[i] = s
			i+=1
def test_group_anagrams():
	input = ["jack","abcd","ab","abcd","ca"]
	group_anagrams(input)
	print(input)

test_group_anagrams()

		
