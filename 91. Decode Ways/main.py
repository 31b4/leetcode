class Solution:
    def numDecodings(self, s: str) -> int:
        forw1 = 1
        forw2 = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                ans = 0
            else:
                ans = forw1

                if i+1 < len(s) and "0" < s[i:i+2] < "27":
                    ans += forw2

            forw2 = forw1
            forw1 = ans

        return forw1
