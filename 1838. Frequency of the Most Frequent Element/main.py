class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        nums.sort()
        
        while j < len(nums):
            k += nums[j]
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
            j += 1

        return j - i
