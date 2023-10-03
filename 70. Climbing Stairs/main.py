class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        # F(n) = F(n-1) + F(n-2)
        prev1, prev2 = 1, 2
        ans = 0
        for i in range(3, n + 1):
            ans = prev1 + prev2
            prev1, prev2 = prev2, ans
        return ans
