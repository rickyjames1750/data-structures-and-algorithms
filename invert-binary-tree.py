# Definition for a binary tree node.
# class TreeNode:
#     def__init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        else:
            right = self.invertTree(root.right)
            left = self.invertTree(root.left) 
            root.right = left
            root.left = right  
        return root