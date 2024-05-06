"""
Peaks and Valleys:In an array of integers,a "peak" is an element which is greater than or equal to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent inte­gers.
For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and valleys.
EXAMPLE
Input: {5, 3, 1, 2, 3}
Output: {5, 1, 3, 2, 3}
"""

def peaks_valleys(array):
	vector = 0
	
	for index,n in enumerate(array):
		before = 0 if index-1 < 0 else index-1
		after = len(array)-1 if index+1 >= len(array) else index+1 
		if n >= array[before] and n >= array[after]:
			vector |= 1 << index
	i = 0
	for index in range(len(array)):
		if is_peak(index):
			swap(array,i,index)
			i++
		if is_valley(index):
			swap(array,i,index
		
		
		 
			
			
			
			
