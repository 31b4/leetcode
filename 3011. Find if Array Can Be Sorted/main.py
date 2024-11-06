class Solution:
    def haveSameSetBits(self, a: int, b: int) -> bool:
        # Python equivalent of __builtin_popcount(a) to count set bits
        return bin(a).count('1') == bin(b).count('1')
    
    def canSortArray(self, nums: list[int]) -> bool:
        N = len(nums)
        times = N
        
        # Perform bubble sort-like operation with condition on set bits
        for _ in range(times):
            for i in range(N - 1):
                if self.haveSameSetBits(nums[i], nums[i + 1]) and nums[i + 1] < nums[i]:
                    # Swap the elements
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        # Check if the array is sorted
        return nums == sorted(nums)
