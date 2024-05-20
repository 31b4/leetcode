class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        # Iterate through all possible subsets
        for i in range(1 << n):
            subset_xor = 0
            for j in range(n):
                # Check if the j-th element is in the i-th subset
                if i & (1 << j):
                    subset_xor ^= nums[j]
            total_sum += subset_xor
        return total_sum
