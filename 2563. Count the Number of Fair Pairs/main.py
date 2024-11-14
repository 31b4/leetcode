class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        
        n = len(nums)
        count = 0
        
        # Step 2: For each element nums[i], use binary search to find the valid range for nums[j]
        for i in range(n - 1):
            # Determine the range of values that nums[j] could be
            min_val = lower - nums[i]
            max_val = upper - nums[i]
            
            # Use binary search to find the range [start, end] in the sorted array
            start = bisect.bisect_left(nums, min_val, i + 1, n)
            end = bisect.bisect_right(nums, max_val, i + 1, n) - 1
            
            # The number of valid pairs for this i is end - start + 1
            if start <= end:
                count += end - start + 1
        
        return count
