class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        for x in set(nums):
            if nums.count(x) > n:
                return x
