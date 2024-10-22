class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        def dfs(r, c, bm, path):
            if self.flag or (r * n + c, bm) in vis:
                # if answer found or state visited, terminate
                return
            vis.add((r * n + c, bm))
            for r1, c1 in (r + 1, c + 2), (r + 1, c - 2), (r - 1, c + 2), (r - 1, c - 2),\
                (r + 2, c + 1), (r + 2, c - 1), (r - 2, c + 1), (r - 2, c - 1):
                if 0 <= r1 < m and 0 <= c1 < n:
                    j = r1 * n + c1
                    if not bm & 1 << j:
                        path1 = path + [(r1, c1)]
                        bm1 = bm | 1 << j
                        if len(path1) == target:
                            # generate answer and flag for early termination
                            self.flag = 1
                            for i, (a, b) in enumerate(path1):
                                ans[a][b] = i
                            return
                        dfs(r1, c1, bm1, path1)
            
        vis = set() # for early termination of visited states
        target = m * n # length of a target path
        ans = [[-1] * n for _ in range(m)]
        self.flag = 0
        ans[r][c] = 0
        dfs(r, c, 1 << r * n + c, [(r, c)])
        return ans
