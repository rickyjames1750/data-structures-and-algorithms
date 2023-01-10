# Definition for a binary tree node.
# class TreeNode:
#       def __init__(self, x):
#            self.val = x
#            self.left = None
#            self.right = None  

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def isBalancedHelper(root):
            if root == None:
                return(True, 0)
            leftB, leftH = isBalancedHelper(root.left)
            rightB, rightH = isBalancedHelper(root.right)
            return (leftB and rightB and abs(leftH - rightH) <= 1 , max(leftH, rightH) + 1)
        return isBalancedHelper(root)[0]