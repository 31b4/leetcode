class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (hi+lo) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
