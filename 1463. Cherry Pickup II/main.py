class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        @cache
        def dp(i,j,k):
            if not 0<=j<=k<n:
                return float('-inf')
            if i==m:
                return 0
            ans=grid[i][j]+(j!=k)*grid[i][k]
            return ans+max(dp(i+1,y,z) for y in (j-1,j,j+1) for z in (k-1,k,k+1))
        return dp(0,0,n-1)          
