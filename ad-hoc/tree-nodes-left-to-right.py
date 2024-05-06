"""
Given a binary tree, we need to write a program to print all leaf nodes of the given binary tree from left to right. 
That is, the nodes should be printed in the order they appear from left to right in the given tree. 
For Example, 



For the above binary tree, the output will be as shown below:
"""
class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

def tree_nodes_left_right(root):
    to_visit = []
    to_visit.append(root)
    leaf = []
    while len(to_visit) > 0:
        current = to_visit.pop()
        if current.left is None and current.right is None:
            leaf.append(current.item)
        else:
            if current.right is not None:
                to_visit.append(current.right)
            if current.left is not None:
                to_visit.append(current.left)
    return leaf


def test_tree_nodes_left_right():
    root = Node(1)
    root.left = Node(2)
    root.left.right = Node(4)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right = Node(8)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)

    print(tree_nodes_left_right(root))
    
test_tree_nodes_left_right()

