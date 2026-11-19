# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        lca = [root]
        
        def find_lca(root):
            if not root:
                return

            lca[0] = root

            if root.val == p.val or root == q.val:
                return
            
            elif root.val < p.val and root.val < q.val:
                find_lca(root.right)

            elif root.val > p.val and root.val > q.val:
                find_lca(root.left)

            else:
                return

        find_lca(root)
        return lca[0]