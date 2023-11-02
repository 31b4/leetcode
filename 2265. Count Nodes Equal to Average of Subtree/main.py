class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        def trav(node):
            su = node.val
            count = 1
            if node.left:
                outsu,outcount = trav(node.left)
                su+=outsu
                count+=outcount
            if node.right:
                outsu,outcount = trav(node.right)
                su+=outsu
                count+=outcount
            
            if count != 0 and node.val == (su//count):
                self.ret+=1
            return su,count
        trav(root)
        return self.ret
