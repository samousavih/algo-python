"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.

note: the successor of a node is the node with the smallest key greater than the key of the input node.
it has two cases: 
1. if the node has a right child, then the successor is the leftmost node of the right child.
2. if the node doesn't have a right child, then the successor is the first parent that is greater than the node.

In the example below if the input is 6 the next node is 8, because 6 doesn't have a right child,
so we move up so we reach a node whichc the current node is the left child of it, so the successor is the parent of the current node.

        8
       / \
      3   10
     / \    \
    1   6    14
       /    
      4   

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