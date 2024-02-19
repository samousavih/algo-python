"""
Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order,
EXAMPLE
Input:find5in[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
Output: 8
"""

def find_rotated(input,number,start,end):
	if start > end:
		return -1
	mid = (end + start) //2
	if input[mid] == number:
		return mid

	if input[mid] < input[end]:
		if number > input[mid] and number <= input[end]:
			return find_rotated(input,number,mid+1,end)
		else:
			return find_rotated(input,number,start,mid-1)
	elif input[mid] > input[start]:
		if number < input[mid] and number >= input[start]:
			return find_rotated(input,number,start,mid-1)
		else:
			return find_rotated(input,number,mid+1,end)
	elif input[mid] == input[end]: 
		if input[mid] != input[start]:
			return find_rotated(input,number,start,mid-1)
		else: 
			item = find_rotated(input,number,start,mid-1)
			if item == -1:
				return find_rotated(input,number,mid+1,end)
			else:
				return item
	else:
		return -1
	return -1
def test_find_rotated():
	assert find_rotated([15,16,19,20,25,1,3,4,5,7,10,14],5,0,11) == 8
	assert find_rotated([2,2,2,3,4,2],3,0,5) == 3	

test_find_rotated()	
   
