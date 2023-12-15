class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        xs = [i for i in range(m) for j in range(n) if grid[i][j]]
        ys = [j for i in range(m) for j in range(n) if grid[i][j]]
        xs.sort()
        ys.sort()
        x, y = xs[len(xs)//2], ys[len(ys)//2]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += abs(i-x) + abs(j-y)
        return res
