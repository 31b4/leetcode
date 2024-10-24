class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base cases
        if not root1 and not root2:  # Both are None
            return True
        if not root1 or not root2:  # One is None and the other is not
            return False
        if root1.val != root2.val:  # Values are not equal
            return False
        
        # Check if the trees are flip equivalent
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        
        return no_flip or flip
