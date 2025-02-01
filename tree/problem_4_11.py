"""
Random Node: You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
""" 
import random


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1
    def get_random_node(self):
        r = random.randint(0, self.size-1)
        return self.find_nth_node(r)

    def find_nth_node(self, r):
        if self == None:
            return None
        left_size = 0 if not self.left else self.left.size
        if r < left_size:
            return self.left.find_nth_node(r)
        elif r == left_size:
            return self
        else:
            return self.right.find_nth_node(r-left_size-1)
        
def test_get_random_node():
    node= Node(2)
    node.size=5
    node.left = Node(1)
    node.left.size = 1
    node.right = Node(3)
    node.right.size = 3
    node.right.left = Node(2.5)
    node.right.left.size=1
    node.right.right = Node(5)
    node.right.right.size=1
    print(node.get_random_node().value)
test_get_random_node()
        




