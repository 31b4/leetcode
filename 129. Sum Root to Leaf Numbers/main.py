class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, path):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                ans += path * 10 + node.val
                return
            dfs(node.left, path * 10 + node.val)
            dfs(node.right, path * 10 + node.val)
        
        ans = 0
        dfs(root, 0)
        return ans
