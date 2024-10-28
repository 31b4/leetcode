class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Sort and convert list to a set for quick lookup
        nums.sort()
        num_set = set(nums)
        
        longest_streak = 0
        
        # Check for square streak starting with each number
        for num in nums:
            streak_length = 0
            current = num
            
            # Continue as long as we find the square in the set
            while current in num_set:
                streak_length += 1
                current = current * current  # Square the current number
            
            # Update longest streak if this one is the longest so far
            if streak_length >= 2:
                longest_streak = max(longest_streak, streak_length)
        
        # If no streak of at least 2 was found, return -1
        return longest_streak if longest_streak >= 2 else -1
