class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            try:
                if nums[i] == val:
                    del nums[i]    
                    i -=1
            except:
                break
            i+=1
