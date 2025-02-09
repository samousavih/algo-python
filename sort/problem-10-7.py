"""
Missing Int: Given an input file with four billion non-negative integers, provide an algorithm to generate an integer that is not contained in the file.
Assume you have 1 GB of memory available for this task.

4B 4G =  2^32  2^8 =256 2^9 = 512 2^10 = 1 MB 2^20 = 1GB 2^30 = 1GB and 2^32 = 4GB

32 bit and 2^5 *2^31 = 2^36
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

