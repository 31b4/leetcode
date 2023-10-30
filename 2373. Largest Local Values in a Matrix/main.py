class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []

        for i in range(n-2):
            row = []
            for j in range(n-2):
                k = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
                row.append(max(grid[i+x][j+y] for x,y in k))
            ans.append(row)
        
        return ans
