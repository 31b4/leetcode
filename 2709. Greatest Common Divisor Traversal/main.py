class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums)==1:return True
        nums = set(nums)
        if 1 in nums:return False
        if len(nums)==1:return True
        
        nums = sorted(nums,reverse=True)

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if gcd(nums[i],nums[j])-1:
                    nums[j]*=nums[i]
                    break
            else:
                return False
        return True
