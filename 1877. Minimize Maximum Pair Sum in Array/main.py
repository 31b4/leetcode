class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        l, r = 0, len(nums) - 1

        min_max_pair_sum = -1

        while l < r:
            current_pair_sum = nums[l] + nums[r]
            min_max_pair_sum = max(min_max_pair_sum, current_pair_sum)

            l += 1
            r -= 1

        return min_max_pair_sum
