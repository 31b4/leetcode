# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        if root.val == target:
            big = root.right
            root.right = None
            small = root
            return [small, big]
        elif root.val < target:
            [small, big] = self.splitBST(root.right, target)
            root.right = small
            return [root, big]
        else:
            [small, big] = self.splitBST(root.left, target)
            root.left = big
            return [small, root]
