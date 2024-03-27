class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:  # If k <= 1, no subarray can satisfy the condition
            return 0
        
        count = 0
        prod = 1  # Product of elements in the current window
        left = 0   # Left pointer of the window
        
        for right, num in enumerate(nums):
            prod *= num  # Expand the window by multiplying the current number
            while prod >= k:  # Shrink the window from the left until the product is less than k
                prod /= nums[left]
                left += 1
            count += right - left + 1  # Add the number of valid subarrays ending at the current position
        
        return count
        
