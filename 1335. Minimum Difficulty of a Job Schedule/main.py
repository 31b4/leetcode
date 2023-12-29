class Solution:
    def minDifficulty(self, jD: List[int], d: int) -> int:
        if len(jD)<d:return -1
        def solve(i,d):
            if i==len(jD):return 100000000
            if d==1:return max(jD[i:])
            if dp[i][d]!=-1:return dp[i][d]
            ans=100000000
            mx=-1
            for j in range(i,len(jD)):
                mx=max(mx,jD[j])
                temp=mx+solve(j+1,d-1)
                ans=min(ans,temp)
            dp[i][d]=ans
            return dp[i][d]
        dp=[[-1 for i in range(d+1)] for i in range(len(jD))]
        return solve(0,d)
