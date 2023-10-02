class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x = {}
        for i in range(len(nums)):
            if nums[i] in x and abs(i - x[nums[i]]) <= k:
                return True
            x[nums[i]] = i
        return False
