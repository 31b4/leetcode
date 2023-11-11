class Solution:
    def maxSpending(self, values ) -> int:
        ans = 0
        for i, k in enumerate(sorted(sum(values, []))):
            ans += (i+1) * k 
        return ans
