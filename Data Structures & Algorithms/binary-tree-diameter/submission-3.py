# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = [0]

        def height(root):

            if not root:
                return 0

            leftheight = height(root.left)

            rightheight = height(root.right)

            diameter[0] = max(diameter[0], leftheight + rightheight)

            return 1 + max(leftheight, rightheight)

        height(root)

        return diameter[0]