# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        def preOrder(root, low, high):
            nonlocal ans
            if not root: return
            if low<=root.val<=high:
                ans+=root.val
            preOrder(root.left, low, high)
            preOrder(root.right, low, high)
        
        preOrder(root, low, high)
        return ans
