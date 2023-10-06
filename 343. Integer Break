class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            n-=1
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        return ans * n 
