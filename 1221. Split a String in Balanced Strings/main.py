class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, ans = 0, 0

        for char in s:
            count += 1 if char == 'R' else -1
            ans += count == 0

        return ans
