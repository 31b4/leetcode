class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: TreeNode)-> None:
            if not root: return
            d[root.val]+=1
            dfs(root.left)
            dfs(root.right)
            return
        d, ans = defaultdict(int), []
        dfs(root)
        mx = max(d.values())

        return [key for key in d if d[key] == mx]
