class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = sum(range(len(nums) + 1))
        actual_sum = sum(nums)
        return expected_sum - actual_sum
