class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums)-sum(set(nums)), len(nums)*(len(nums)+1)//2-sum(set(nums))]
