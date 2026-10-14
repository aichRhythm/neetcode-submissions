# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# go through each node
# check it's left and right sub tree
# see if height diff is abs 1
# if not return false directly

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def isNodeBalanced(root):

            if root is None:
                return [True, 0]
            
            left, right = isNodeBalanced(root.left), isNodeBalanced(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return isNodeBalanced(root)[0]

