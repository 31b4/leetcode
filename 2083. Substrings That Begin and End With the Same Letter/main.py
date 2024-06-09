class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
            ans += d[c]
        return ans
