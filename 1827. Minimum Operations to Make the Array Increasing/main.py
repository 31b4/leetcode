class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev = nums[0]
        res = 0
        for x in nums[1:]:
            if x <= prev:
                diff = abs(x-prev)+1
                prev = x + diff
                res += diff
            else:
                prev = x
        return res
            
