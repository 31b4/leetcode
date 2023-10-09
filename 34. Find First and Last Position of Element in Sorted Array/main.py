class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not target in nums:
            return [-1,-1]
        if len(nums) == 1:
            return [0,0]
        ans = [-1,-1]
        for i,x in enumerate(nums):
            if ans[0] == -1 and x == target:
                ans[0] = i
            elif ans[0] != -1 and x != target:
                ans[1]=i-1
                return ans
        ans[1]= len(nums)-1
        return ans
