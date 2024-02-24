"""
Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size method. It does, however, have an elementAt(i) method that returns the element at index i in 0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data structure only supports positive integers.) Given a Listy which contains sorted, positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index.
"""

def elementAt(a,i):
	if i >= len(a):
		return -1
	else:
		return a[i]	
def find_listy(a,number):
	end = 1
	while elementAt(a,end-1) != -1:
		end*=2
	print(end)
	return find_listy_util(a,number,0,end-1)

def find_listy_util(a,number,start,end):
	if start > end: 
		return -1
	mid = (start+end)//2
	if elementAt(a,mid) == number:
		return mid
	if elementAt(a,mid) != -1:
		if elementAt(a,mid) < number:
			return find_listy_util(a,number,start,mid-1)
		else:
			return find_listy_util(a,number,mid+1,end)
	else:
		return find_listy_util(a,number,start,mid-1)
	return -1

def test_find_listy():
	assert find_listy([1,2,3,4,7,8],4) == 3

test_find_listy()
