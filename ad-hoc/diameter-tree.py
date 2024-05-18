# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter,_ = self.diameterOfBinaryTreeRec(root)
        return diameter

    def diameterOfBinaryTreeRec(self,root):
        if root == None:
            return 0,0
        leftDiameter,leftDepth = self.diameterOfBinaryTreeRec(root.left)
        rightDiameter,rightDepth = self.diameterOfBinaryTreeRec(root.right)
        return max(leftDiameter,rightDiameter,leftDepth+rightDepth),max(leftDepth,rightDepth)+1


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