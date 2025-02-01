"""
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
EXAMPLE
Input:
        2
       / \
      1   3
Output: {2, 1, 3}, {2, 3, 1} 

           2
       /       \
      1         3
    /  \      /   \
   0    1.5  2.5   4

output = {2, 1,0,1.5 , 3,2.5,4 }, {2, 1,3,0,1.5}
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

def possible_arrays(tree):
    if tree == None:
        return []
    result = []
    lef_comb = possible_arrays(tree.left)
    right_comb = possible_arrays(tree.right)
    mix_comb=mix(lef_comb,right_comb)
    if len(mix_comb) == 0:
        result = [[tree.value]]
    for comb in mix_comb:
        result.append([tree.value]+comb)
    return result
    
def mix(array1,array2):
    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1
    
    if len(array1[0]) == 0:
        return array2
    if len(array2[0]) == 0:
        return array1

    array1_without_first = []
    array2_without_first = []
    for element in array1:
        array1_without_first.append(element[1:])
    for element in array2:
        array2_without_first.append(element[1:])
    first=mix(array1_without_first,array2)
    second=mix(array1,array2_without_first)
    result = []
    for element in first:
        result.append([array1[0][0]]+element)    
    for element in second:
        result.append([array2[0][0]]+element)    

    return result

def possible_arrays_2(tree):
    if tree == None:
        return []
    result = []
    if tree.left == None and tree.right == None:
        result.append([tree.value])
        return result

    lef_comb = possible_arrays_2(tree.left)
    right_comb = possible_arrays_2(tree.right)

    for array in lef_comb:
        result.append([tree.value]+array)
    
    
    for array in right_comb:
        result.append([tree.value]+array)
     
    return result


def test_possible_arrays():
    node= Node(2)
    node.left = Node(1)
    node.right = Node(3)
    node.right.left = Node(2.5)
    node.right.right = Node(5)
    print(possible_arrays(node))
    print(possible_arrays_2(node))
test_possible_arrays()


    
