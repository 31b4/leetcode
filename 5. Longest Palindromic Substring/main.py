class Solution:
    def longestPalindrome(self, s: str) -> str:
        t,ans="",""
        size=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                t+=s[j]
                if t==t[::-1] and len(t)>size:
                    ans=t
                    size=len(t)
            t=""
        return ans
