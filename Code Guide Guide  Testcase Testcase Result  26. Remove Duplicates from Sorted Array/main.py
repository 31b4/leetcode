class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            try:
                if nums[i] in nums[i+1:]:
                    del nums[i]
                else: 
                    i += 1
            except:
                break
