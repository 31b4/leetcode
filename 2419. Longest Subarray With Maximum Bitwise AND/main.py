class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        maxLen, xMax, Len=0, 0, 0
        i=0
        while i<n:
            while i<n and nums[i]==xMax:
                i+=1
                Len+=1
            if i==n or nums[i]<xMax:
                maxLen=max(maxLen, Len)
                Len=0
            else:
                xMax=nums[i]
                maxLen=Len=1
            i+=1
        return maxLen
        
