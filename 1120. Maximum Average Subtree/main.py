# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        def fn(node): 
            """Return sum, count and max average of subtree rooted at node."""
            if not node: return 0, 0, 0
            ls, ln, lv = fn(node.left)
            rs, rn, rv = fn(node.right)
            s = ls + node.val + rs
            n = ln + 1 + rn 
            return s, n, max(s/n, lv, rv)
            
        return fn(root)[2]
