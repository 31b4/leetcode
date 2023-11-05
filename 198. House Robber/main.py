class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)

        M = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            M = M[1], max(nums[i]+M[0], M[1])
        return M[1]
