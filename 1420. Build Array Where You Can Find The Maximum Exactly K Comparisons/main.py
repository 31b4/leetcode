class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        def dfs(n,m,k,i,currentMax,currentCost,dp):
            if i == n:
                return 1 if k == currentCost else 0
            if dp[i][currentMax][currentCost] != None:
                return dp[i][currentMax][currentCost]
            ans = 0
            for num in range(1,m+1):
                newCost = currentCost
                newMax = currentMax
                if num > currentMax:
                    newCost += 1
                    newMax = num
                if newCost > k:
                    break
                ans += dfs(n, m, k, i+1, newMax, newCost, dp)
                ans %= 1000000007
            dp[i][currentMax][currentCost] = ans
            return ans
        dp = [[[None for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
        return dfs(n, m, k, 0, 0, 0, dp)
