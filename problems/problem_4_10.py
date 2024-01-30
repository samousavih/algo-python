"""
Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical. 
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def is_subtree(T1,T2):
    to_visit = []
    to_visit.append(T1)
    while len(to_visit)>0:
        current=to_visit.pop()
        if current is not None:
            if current.value == T2.value:
                if is_same(current,T2):
                    return True    
            to_visit.append(current.left)
            to_visit.append(current.right)
    return False

def is_same(T1,T2):
    to_visit = []
    if T1.value != T2.value:
        return False
    to_visit.append((T1,T2))
    while len(to_visit)>0:
        current_t1,current_t2= to_visit.pop()
        if current_t1 is not None and current_t2 is None:
            return False
        if current_t1 is None and current_t2 is not None:
            return False
        if current_t1 is not None and current_t2 is not None:
            to_visit.append((current_t1.left,current_t2.left))
            to_visit.append((current_t1.right,current_t2.right))
    return True

def test_is_sub_tree():
    tree1 = Node(1)
    tree1.left = Node(2)
    tree1.right = Node(3)

    tree2 = Node(2)
    tree3 = Node(5)
    assert is_subtree(tree1,tree2) == True
    assert is_subtree(tree1,tree3) == False

test_is_sub_tree()
        
        
        


