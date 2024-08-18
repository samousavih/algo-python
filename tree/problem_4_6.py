"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
"""

from bst import BST_Node

def successor(node:BST_Node):
    if node.right != None:
        if node.right.left != None:
            next = node.right.left     
            while next.left != None:
                next = next.left
            return next
        return node.right
    parent = node.parent
    child = node
    while parent and parent.right == child:
        child = parent
        parent = child.parent
    return parent


def test_in_order_successor(successor):
    bst = BST_Node(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    # Test all nodes
    inputs = [5, 9, 11, 12, 14, 20, 25]
    outputs = inputs[1:]
    outputs.append(None)

    for x, y in zip(inputs, outputs):
        test = bst.get_node(x)
        succ = successor(test)
        if succ is not None:
            assert succ.value == y, f"{succ.value} == {y} of {test.value}"
        else:
            assert succ == y        

test_in_order_successor(successor)