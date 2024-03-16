class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}                                # dic record: count(the times we met 1 - the time we met 0) : idx
        count = 0                                   # lets say count == 3, it means until this idx, if 0 appeared x time, 1 appeared x+3 time
        res = 0                                     # So, once count == 3 appears at the other position again,
        
        for i in range(len(nums)):                  # let's say 0 appeared y time, 1 appeared y+3 time
            if nums[i] == 0:                        # So for the interval between these two idx, 0 and 1 both appear (y-x) time!
                count -= 1
            if nums[i] == 1:
                count += 1
            
            if count in dic:                        # Same count indicate that the interval between these tow idx have same amount 0 and 1.
                res = max(res, i - dic[count])
            else:                                   # Otherwise, we record the idx of the count when first time we met it.
                dic[count] = i
        
        return res
