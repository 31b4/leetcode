class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        sv = 0
        for num in nums:
            if num == 1:
                sv += 1
            else:
                res = max(res,sv)
                sv = 0
        return max(res,sv)
