"""
Rank from Stream:Imagine you are reading in a stream of integers.Periodically,you wish to be able to look up the rank of a number x (the number of values less than or equal to x). Implement the data structures and algorithms to support these operations.
That is, implement the method track ( int x), which is called when each number is generated, and the method getRankOfNumber(int x), which returns the number of values less than or equal to x (not including x itself).
EXAMPLE
Stream (in order of appearance): 5, getRankOfNumber(l) 0 getRankOfNumber(3) = 1 getRankOfNumber(4) 3 Hints:#301, #376, #392
1, 4, 4,
5, 9,
7, 13, 
"""

class rank_node():
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
		self.rank = 0
	def track(self,x):
		if x <= self.value:
			self.rank+=1
			if self.left is not None:
				self.left.track(x)
			else:
				self.left = rank_node(x)
				self.left.rank = 0
		else:
			if self.right is not None:
				self.right.track(x)
			else:
				self.right = rank_node(x)
				self.right.rank = self.rank+1
	def get_rank_of_number(self,x):
		if self is  None:
			return -1
		if x == self.value:
			return self.rank
		elif x <= self.value:
			return self.left.get_rank_of_number(x)
		else:
			return self.right.get_rank_of_number(x)

def test_rank_node():
	node = None
	for x in [1,4,4,5,9,7,13,3]:
		if node is None:
			node = rank_node(x)
		else:
			node.track(x)
	assert node.get_rank_of_number(1) == 0
	assert node.get_rank_of_number(4) == 3

test_rank_node()
