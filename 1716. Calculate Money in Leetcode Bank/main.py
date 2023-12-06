class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        sv = 0
        for i in range(1, n+1):
            res = i % 7
            if res % 7 == 0:
                res += 7
            ans += sv + res
            if i % 7 == 0:
                sv += 1
        return ans
        
