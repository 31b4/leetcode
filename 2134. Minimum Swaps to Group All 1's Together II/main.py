class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums) 
        if k == 0 or k == n:
            return 0  

        extended_nums = nums + nums[:k-1]
        current_zeros = sum(1 for i in range(k) if extended_nums[i] == 0)
        min_zeros = current_zeros
        
        for i in range(1, n):
            if extended_nums[i-1] == 0:
                current_zeros -= 1
            if extended_nums[i+k-1] == 0:
                current_zeros += 1
            min_zeros = min(min_zeros, current_zeros)
        
        return min_zeros
        
