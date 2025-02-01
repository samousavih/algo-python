

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree. 
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter,_ = self.diameterOfBinaryTreeRec(root)
        return diameter

    def diameterOfBinaryTreeRec(self,root):
        if root == None:
            return 0,0
        leftDiameter,leftHeight = self.diameterOfBinaryTreeRec(root.left)
        rightDiameter,rightHeight = self.diameterOfBinaryTreeRec(root.right)
        height = max(leftHeight,rightHeight)+1
        diameter = max(leftDiameter,rightDiameter,height)
        return diameter,height


"""
Notice here "res = [0]" an array is used to make it mutable as variables of int,string etc are immutable
https://nedbatchelder.com/text/names.html
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Define a recursive function to calculate the diameter
        def diameter(node, res):
            # Base case: if the node is None, return 0
            if not node:
                return 0
            
            # Recursively calculate the diameter of left and right subtrees
            left = diameter(node.left, res)
            right = diameter(node.right, res)

            # Update the maximum diameter encountered so far
            res[0] = max(res[0], left + right)
            
            # Return the depth of the current node
            return max(left, right) + 1
        
        # Initialize a list to hold the maximum diameter encountered
        res = [0]
        # Call the diameter function starting from the root
        diameter(root, res)
        # Return the maximum diameter encountered
        return res[0]
    