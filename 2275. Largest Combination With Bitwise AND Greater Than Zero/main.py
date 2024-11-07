class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # We only need 24 bits because max(candidates) <= 10^7, which is < 2^24
        bit_counts = [0] * 24
        
        # Count the number of times each bit position is set to 1 across all numbers
        for number in candidates:
            for i in range(24):
                if number & (1 << i):  # Check if the i-th bit is set
                    bit_counts[i] += 1
        
        # The result is the maximum count found in any bit position
        return max(bit_counts)
