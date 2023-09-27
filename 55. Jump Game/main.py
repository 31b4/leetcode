class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dist = 0
        for i,x in enumerate(nums):
            if i > dist:
                return False
            dist = max(dist, x+i)
        return True
