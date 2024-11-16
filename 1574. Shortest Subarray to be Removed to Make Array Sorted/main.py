class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Step 1: Find the longest non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        
        # If the entire array is non-decreasing
        if left == n - 1:
            return 0
        
        # Step 2: Find the longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Step 3: The minimum elements to remove is the minimum of:
        # 1. Removing all elements from right of 'left' or left of 'right'
        result = min(n - left - 1, right)
        
        # Step 4: Try to merge the prefix and suffix by checking if we can connect arr[left] and arr[right]
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1
        
        return result
