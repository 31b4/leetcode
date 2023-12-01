class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        res = -1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] < k:
                    res = max(res,nums[i] + nums[j])
        return res
