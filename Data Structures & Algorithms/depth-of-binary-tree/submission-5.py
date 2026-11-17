# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        leftRoot, rightRoot = root.left, root.right
        leftHeight = self.maxDepth(leftRoot)
        rightHeight = self.maxDepth(rightRoot)
        return 1 + max(leftHeight, rightHeight)