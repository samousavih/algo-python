"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
"""
"""
Note how data structure impacts the complexity of algorithm, using a recursive tree structure makes a recursive implementation lot easier
"""
import math
def create_bs_min_hight(array,start,end):
    if end < start:
        return []

    root_index = math.ceil((start+end)/2)
    
    root = array[root_index]
    tree = [(root,None)]
    
    left_tree = create_bs_min_hight(array,start,root_index-1)
    right_tree = create_bs_min_hight(array,root_index+1,end)

    if len(left_tree)>0:
        left_root,_ = left_tree[0]
        left_tree[0] = (left_root,root)

    if len(right_tree)>0:
        right_root,_ = right_tree[0]
        right_tree[0] = (right_root,root)
    
    tree = tree+right_tree+left_tree
    return tree

class Node:
    def __init__(self,item):
        self.value = item
        self.right = None
        self.left = None
    def __str__(self):
        temp = ""
        if self.left:
            temp+=str(self.left)
        temp+=str(self.value)
        if self.right:
            temp+=str(self.right)
        return temp

def create_bs_min_hight_with_tree(array,start,end):
    if end < start:
        return None
    mid = (start+end)//2
    root= Node(array[mid])
    root.left = create_bs_min_hight_with_tree(array,start,mid-1)
    root.right = create_bs_min_hight_with_tree(array,mid+1,end)
    return root
    
def test_get_minimal_tree():
    array = [1,5,6,8,9,12]
    tree = create_bs_min_hight(array,0,len(array)-1)
    print(tree)
    assert tree == [(8, None), (12, 8), (9, 12), (5, 8), (6, 5), (1, 5)]

def test_get_minimal_tree_with_tree():
    array = [1,5,6,8,9,12]
    tree = create_bs_min_hight_with_tree(array,0,len(array)-1)
    assert str(tree) == "1568912"
    assert tree.value == 6
    assert tree.left.value == 1
    assert tree.right.value == 9

test_get_minimal_tree()
test_get_minimal_tree_with_tree()



