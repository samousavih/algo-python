"""
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
"""

def merge(a,b):
	i = len(a)-len(b)-1
	j = len(b)-1
	k = len(a)-1
	while i >= 0 and j >= 0:
		if a[i]>=b[j]:
			a[k] = a[i]
			k-=1
			i-=1
		else:
			a[k] = b[j]
			k-=1
			j-=1

def test_merge():
	a=[1,4,5,7,0,0,0]
	b=[2,3,6]
	merge(a,b)
	assert a == [1,2,3,4,5,6,7]
test_merge()
