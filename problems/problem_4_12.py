"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes). 
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def number_of_path_helper(tree,sum_so_far,target_sum,number_of_sums):
    if not tree:
        return 0
    n_paths = 0
    sum_so_far+=tree.value
    if sum_so_far - target_sum in number_of_sums:
        n_paths = number_of_sums[sum_so_far - target_sum]
    if sum_so_far == target_sum:
        n_paths+=1
    if  sum_so_far in number_of_sums:
        number_of_sums[sum_so_far]+=1
    else:
        number_of_sums[sum_so_far]=1
    n_paths+=number_of_path_helper(tree.left,sum_so_far,target_sum,number_of_sums)
    n_paths+=number_of_path_helper(tree.right,sum_so_far,target_sum,number_of_sums) 
    number_of_sums[sum_so_far]-=1
    if number_of_sums[sum_so_far] ==0:
        del number_of_sums[sum_so_far]
    return n_paths
def number_of_path(tree, target_sum):
    return number_of_path_helper(tree,0,target_sum,{})

def test_number_of_paths():
    node= Node(2)
    node.left = Node(1)
    node.left.left = Node(1)
    node.left.left.left = Node(1)
    node.right = Node(3)
    node.right.left = Node(2.5)
    node.right.right = Node(5)
    assert number_of_path(node,5) == 3
    assert number_of_path(node,3) == 3

test_number_of_paths()



