class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[float('-inf')] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                sv = nums1[i-1] * nums2[j-1]
                dp[i][j] = max(dp[i][j], sv, dp[i-1][j], dp[i][j-1], sv + dp[i-1][j-1])       
        return dp[n][m]
