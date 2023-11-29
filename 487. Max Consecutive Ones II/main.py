class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr, prev, seenZero = 0, 0, 0
        for num in nums:
            if num == 0:
                seenZero = 1
                prev = curr
                curr = 0
            else:
                curr += 1
            res = max(res, curr+ prev+ seenZero)
        return res
