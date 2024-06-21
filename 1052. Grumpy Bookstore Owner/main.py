class Solution:
    def maxSatisfied(self, customers: list, grumpy: list, minutes: int) -> int:
        n = len(customers)
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
        
        unsatis = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                unsatis += customers[i]
        
        max_ = unsatis
        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                unsatis -= customers[i - minutes]
            if grumpy[i] == 1:
                unsatis += customers[i]
            max_ = max(max_, unsatis)
        
        return ans + max_
