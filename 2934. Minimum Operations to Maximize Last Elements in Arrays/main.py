
class Solution:
    def minOperations(self, nums1, nums2):
        n = len(nums1)

        dp = [[0, 1] for _ in range(n)]
        inf = 10**9
        for i in range(n-2, -1, -1):
            dp[i][0] = dp[i][1] = inf

            if nums1[i] <= nums1[n-1] and nums2[i] <= nums2[n-1]:
                dp[i][0] = min(dp[i][0], dp[i+1][0])
                dp[i][1] = min(dp[i][1], dp[i+1][1] + 1)

            if nums1[i] <= nums2[n-1] and nums2[i] <= nums1[n-1]:
                dp[i][0] = min(dp[i][0], dp[i+1][0] + 1)
                dp[i][1] = min(dp[i][1], dp[i+1][1])

        best = min(dp[0][0], dp[0][1])

        if best > n:
            return -1
        return best
