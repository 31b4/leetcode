class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        N = len(s)
        l = 0
        total = 0

        lookup = defaultdict(int)

        for r in range(N):
            lookup[s[r]] += 1

            while lookup[s[r]] > 1:
                lookup[s[l]] -= 1
                l += 1

            total += r - l + 1

        return total
        
