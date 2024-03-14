class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        sum_count = defaultdict(int)
        
        for num in nums:
            prefix_sum += num
            if prefix_sum == goal:
                count += 1
            if prefix_sum - goal in sum_count:
                count += sum_count[prefix_sum - goal]
            sum_count[prefix_sum] += 1
        
        return count
