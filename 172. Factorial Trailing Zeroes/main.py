class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n >= 5:
            n //= 5 
            ans += n
        return ans
