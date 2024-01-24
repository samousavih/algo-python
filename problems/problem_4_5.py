"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(root):
    to_visit = []
    to_visit.append(root)

    while len(to_visit)>0:
        current = to_visit.pop()
        if current.left:
            if current.left.value <= current.value:
                to_visit.append(current.left)
            else:
                return False
        if current.right :
            if current.right.value > current.value:
                to_visit.append(current.right)
            else:
                return False
    return True

def test_is_bst():
    root = Node(4)
    root.left = Node(3)
    root.right = Node(6)
    assert is_bst(root) == True

test_is_bst()