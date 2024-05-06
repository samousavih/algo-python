"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""

def create_depth_linked_lists(node,depth,depth_linked_lists):
    if node == None:
        return
    depth_linked_lists[depth+1] = None
    create_depth_linked_lists(node.left,depth+1,depth_linked_lists)
    create_depth_linked_lists(node.right,depth+1,depth_linked_lists)
    
    if depth_linked_lists[depth] == None:
        depth_linked_lists[depth] = LinkedList(node.value)
    else:
        depth_linked_lists[depth].next = LinkedList(node.value) 

class Node:
    def __init__(self, item):
        self.value = item
        self.left = None
        self.right = None
class LinkedList:
    def __init__(self, item):
        self.value = item
        self.next = None

def test_create_depth_linked_lists():
    root = Node(5)
    root.left = Node(6)
    root.left.right = Node(7)
    root.left.left = Node(8)
    result = {}
    result[0] = None
    create_depth_linked_lists(root,0,result)
    
    assert result[2].value == 8
    assert result[2].next.value == 7
    assert result[0].value == 5
test_create_depth_linked_lists()
