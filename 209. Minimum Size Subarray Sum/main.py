class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums)
        if sum(nums) < target:
            return 0
        sv = 0
        j = 0
        for i,val in enumerate(nums):
            sv+=val
            while sv >= target:
                sv-=nums[j]
                ans = min(ans,i-j+1)
                j+=1
        return ans
