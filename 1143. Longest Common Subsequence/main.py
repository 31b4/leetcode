
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            return self.LCS(text1, text2)
        return self.LCS(text2, text1)

    def LCS(self, s1: str, s2: str) -> int:
        dp = [0] * (len(s1) + 1)

        for i in range(1, len(s2) + 1):
            prev = 0
            for j in range(1, len(s1) + 1):
                temp = dp[j]
                if s1[j - 1] == s2[i - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j - 1], dp[j])
                prev = temp
        return dp[len(s1)]
