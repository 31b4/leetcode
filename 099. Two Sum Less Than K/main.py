class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] < k:
                    res.append(nums[i] + nums[j])
        return -1 if not len(res) else max(res)
