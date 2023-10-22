class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res=nums[k]
        i=k
        j=k
        min_val=nums[k]

        while i>0 or j<len(nums)-1:
            if i==0:
                j+=1
                min_val=min(min_val,nums[j])
            elif j==len(nums)-1:
                i-=1
                min_val=min(min_val,nums[i])
            elif nums[i-1]>nums[j+1]:
                i-=1
                min_val=min(min_val,nums[i])
            else:
                j+=1
                min_val=min(min_val,nums[j])
            res=max(res,min_val*(j-i+1))
        return res
