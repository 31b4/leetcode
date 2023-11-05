class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1

        s = str(abs(x))
        x = int(s[::-1])

        return x*flag if x < 2**31 else 0
