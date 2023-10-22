class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        min_sum = float('inf')

        for i in range(1, len(nums) - 1):
            for j in range(i):
                for k in range(i + 1, len(nums)):
                    if nums[j] < nums[i] and nums[i] > nums[k]:
                        current_sum = nums[j] + nums[i] + nums[k]
                        min_sum = min(min_sum, current_sum)

        if min_sum == float('inf'):
            return -1

        return min_sum




