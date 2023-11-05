class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return k * max(nums) + k * (k - 1) // 2
