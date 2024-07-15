class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        
        def fn(node):
            """Traverse the tree post-order."""
            nonlocal ans 
            if not node: return False, -inf
            ltf, lv = fn(node.left)
            rtf, rv = fn(node.right)
            
            if node.val in (p, q) or ltf and rtf: 
                if ltf: ans += lv + 1
                if rtf: ans += rv + 1
                return True, 0
            return ltf or rtf, max(lv, rv) + 1
                
        ans = 0
        fn(root)
        return ans 
