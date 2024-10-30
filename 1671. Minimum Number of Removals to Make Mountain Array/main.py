class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Compute LIS up to each index
        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        # Step 2: Compute LDS from each index
        lds = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        # Step 3: Calculate the minimum removals
        max_mountain_len = 0
        for i in range(1, n - 1):  # i should be a peak, so we avoid the first and last element
            if lis[i] > 1 and lds[i] > 1:  # A valid peak needs both lis and lds > 1
                max_mountain_len = max(max_mountain_len, lis[i] + lds[i] - 1)
        
        # The minimum removals needed to form a mountain array
        return n - max_mountain_len
