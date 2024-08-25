
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def pot(root):
            if root:
                pot(root.left)
                pot(root.right)
                res.append(root.val)
        pot(root)
        return res
