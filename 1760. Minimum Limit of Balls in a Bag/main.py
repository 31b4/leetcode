class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Helper function to determine if a penalty is feasible
        def canAchievePenalty(penalty):
            operations = 0
            for balls in nums:
                # Count how many splits are required to make balls <= penalty
                if balls > penalty:
                    operations += (balls - 1) // penalty
            return operations <= maxOperations
        
        # Binary search for the minimum penalty
        left, right = 1, max(nums)  # Penalty can range from 1 to max(nums)
        while left < right:
            mid = (left + right) // 2
            if canAchievePenalty(mid):
                right = mid  # Try for a smaller penalty
            else:
                left = mid + 1  # Increase the penalty
        return left
