class Solution:
    def tree2str(self, r: Optional[TreeNode]) -> str:
        if not r:
            return ''

        s = f'{r.val}'
        if r.left or r.right:
            s += f'({self.tree2str(r.left)})'
        if r.right:
            s += f'({self.tree2str(r.right)})'
        
        return s
