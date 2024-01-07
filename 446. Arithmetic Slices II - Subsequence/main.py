class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums);ans = 0
        dp = defaultdict(Counter)
        for i in range(1,n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] += dp[j][d] + 1
            ans += sum(dp[i].values()) - i
        return ans
