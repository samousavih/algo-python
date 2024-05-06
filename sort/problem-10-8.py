"""
Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000.
The array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory available, how would you print all duplicate elements in the array?
"""

def find_duplicates(array):
	map = [0] * 1000
	
	for n in array:
		index = n//32
		bit = n%32
		if map[index] & 1 << bit != 0:
			print(n)
		else:
			map[index] |= 1 << bit
	

def test_find_duplicates():
	find_duplicates([1,3,5,6,10,1,5])

test_find_duplicates()
			
