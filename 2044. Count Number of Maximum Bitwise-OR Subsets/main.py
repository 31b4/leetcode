from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Find the maximum possible bitwise OR of the entire array
        max_or = 0
        for num in nums:
            max_or |= num
        
        # Step 2: Helper function to recursively explore subsets and count those with max OR
        def backtrack(index, current_or):
            if index == len(nums):
                return 1 if current_or == max_or else 0
            # Case 1: Include the current element in the subset
            include = backtrack(index + 1, current_or | nums[index])
            # Case 2: Exclude the current element from the subset
            exclude = backtrack(index + 1, current_or)
            return include + exclude
        
        # Step 3: Start backtracking from index 0 and initial OR value 0
        return backtrack(0, 0)
