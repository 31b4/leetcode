# nums - integer array
# 
# return the largest in that only occurs once
# or -1 if it doesn't exist

from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_frequency = defaultdict(int)
        largest_uniq_num = -1

        for num in nums:
            num_frequency[num] += 1
        
        for num, freq in num_frequency.items():
            if freq == 1:
                largest_uniq_num = max(largest_uniq_num, num)
        
        return largest_uniq_num
        
