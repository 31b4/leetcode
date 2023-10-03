class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for x in set_nums:
            if nums.count(x) == 1:
                return x
