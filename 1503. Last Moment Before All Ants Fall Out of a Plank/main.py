class Solution:
    def getLastMoment(self, n, left, right):
        ans = 0
        for i in left:
            ans = max(ans, abs(0 - i))
            
        for i in right:
            ans = max(ans, abs(n - i))
        
        return ans
