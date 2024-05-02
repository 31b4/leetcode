class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] > 0 and -nums[i] in nums:
                return nums[i]
        return -1  # If no such pair found
