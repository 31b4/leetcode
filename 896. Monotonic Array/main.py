class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sortedList = sorted(nums)
        reversedSorted = sorted(nums)
        reversedSorted.reverse()
        return sortedList == nums or reversedSorted == nums
