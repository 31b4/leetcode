class Solution:
    def maxScore(self, s: str) -> int:
        return s.count('1') + max(accumulate((c=='0')-(c=='1') for c in s[:-1]))
