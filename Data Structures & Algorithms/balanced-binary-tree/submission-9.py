# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        balanced = [True]

        def height(root):
            if not root:
                return 0
            leftheight = height(root.left)
            rightheight = height(root.right)
            if abs(leftheight - rightheight) > 1:
                balanced[0] = False
            return 1 + max(leftheight, rightheight)

        height(root)
        return balanced[0]