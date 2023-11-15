class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        result, prefix, sum_dishes = 0, 0, 0
        
        for i in range(len(satisfaction)):
            prefix += satisfaction[i]
            sum_dishes += prefix
            result = max(result, sum_dishes)
        
        return result
