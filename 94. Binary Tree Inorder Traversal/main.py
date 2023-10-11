class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []      
        return self.inorderTraversal(root.left)+[root.val]  + self.inorderTraversal(root.right)
