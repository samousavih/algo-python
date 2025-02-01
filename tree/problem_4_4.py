"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""

def check_tree_is_balance(root):
    if root == None:
        return True,0
    left_is_balanced,left_hight =  check_tree_is_balance(root.left)
    right_is_balanced,right_hight = check_tree_is_balance(root.right)
    
    hight = max(right_hight,left_hight)+1
    
    if not right_is_balanced or not left_is_balanced:
        return False,hight
    elif abs(right_hight - left_hight) > 1:
        return False,hight
    
    return True,hight


class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

def test_check_tree_is_balance():
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(4)
    result,_= check_tree_is_balance(root)
    assert result == False

    root = Node(1)
    root.left = Node(3)
    root.right = Node(4)
    result,_= check_tree_is_balance(root)
    assert result == True

test_check_tree_is_balance()