"""
Missing Int: Given an input file with four billion non-negative integers, provide an algorithm to generate an integer that is not contained in the file. Assume you have 1 GB of memo ry available for this task.
"""

def find_missing_int():

	map = [0]*(2**31)

	for n in read_file():
		index = n//32
		bit = n%32
		map[index] |= 1 << bit
	for index,item in enumerate(map):
		for bit in range(32):
			if ~item & 1 << bit == 1:
				return index * 32 + bit
	return None   	
		
def read_file():
	a=[x for x in range(4001)] + [x for x in range(4002,10000)]
	for x in a:
		yield x
def test_find_missing_int():
	#print(find_missing_int())
	assert find_missing_int() not in list(read_file()) 

test_find_missing_int()

