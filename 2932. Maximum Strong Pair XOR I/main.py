class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            for y in nums:
                if abs(x-y) <= min(x,y):
                    ans = max(ans, x^y)
        return ans
