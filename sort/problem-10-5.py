"""
Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.

"""

def sparse_search(input,key):
	n = len(input)
	start = 0
	end = n-1

	while start <= end:
		mid = (start+end)//2
		if input[mid] == "":
			goLeft = goRight = mid
			while input[goLeft] == "" and input[goRight] == "":
				if goLeft > start:
					goLeft-=1
				if goRight < end:
					goRight+=1
				if goLeft <= start and goRight >=end:
					return -1
			if input[goLeft] != "":
				mid = goLeft
			else:
				mid = goRight
		if input[mid] == key:
			return mid
		elif input[mid] < key:
			start = mid+1
		else:	
			end = mid-1
	return -1

def test_sparse_search():
	assert sparse_search(["at","","","","ball","","","car","","","dad","",""],"ball") == 4
	assert sparse_search(["","",""],"ball") == -1

test_sparse_search()

	
			
					
		
	
