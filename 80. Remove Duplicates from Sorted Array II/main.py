class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            try:
                if nums[i+2] == nums[i]:
                    db = 0
                    for j in range(i+2,len(nums)):
                        if nums[j] == nums[i]:
                            db +=1
                        else:
                            break
                
                    for _ in range(db):
                        del nums[i]
                    if db == 0:
                        i+=1
                else:
                    i+=1
            except:
                break
