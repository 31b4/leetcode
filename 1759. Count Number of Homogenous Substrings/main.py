class Solution:
    def countHomogenous(self, s: str) -> int:
        res, l = 0, 0

        for i, c in enumerate(s):
            if c == s[l]:
                res += i - l + 1
            else:
                l = i
                res += 1

        return res % (pow(10, 9) + 7)
