"""
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree. 
"""

def common_ancestor(node1, node2, tree):
    
    depth1 = get_depth(node1,tree)
    depth2 = get_depth(node2,tree)
    delta = abs(depth1-depth2)
    same_level_node1 = node1
    same_level_node2 = node2
    if delta > 0:
        if depth2 > depth1:
            for _ in range(delta):
                same_level_node1 = tree[same_level_node1]
        else:
            for _ in range(delta):
                same_level_node2 = tree[same_level_node2]

    while same_level_node1 != same_level_node2:
        same_level_node1 = tree[same_level_node1]
        same_level_node2 = tree[same_level_node2]
    return same_level_node1

def get_depth(node,tree):
    depth = 0
    while node != tree[node]:
        node = tree[node]
        depth +=1
    return depth

def test_common_ancestor():
    tree = {1:2,3:2,2:5,6:5,5:5}
    assert common_ancestor(1,6,tree) == 5
    tree = {1:2,3:2,2:5,6:5,5:5}
    assert common_ancestor(1,3,tree) == 2
    tree = {1:2,3:2,2:5,6:5,5:5}
    assert common_ancestor(1,3,tree) == 2
test_common_ancestor()

    