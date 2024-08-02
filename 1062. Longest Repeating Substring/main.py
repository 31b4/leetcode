class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1,n):
            if s[i-ans:i+1] in s[:i]: ans+=1
        return ans
        
