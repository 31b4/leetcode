class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # nums = [3,2,1,2,1,7]
        #        [1,1,2,2,3,7]

        # mySet = set({ num for num in nums }), 2+4
        nums.sort()
        numTracker = 0
        minIncreament = 0

        for num in nums:
            numTracker = max(numTracker, num)
            minIncreament += numTracker - num
            numTracker += 1
        return minIncreament
