class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            self.val += node.val
            node.val = self.val
            dfs(node.left)
        
        dfs(root)
        return roo
