class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        before = 0
        after = len(s)-1
        l = list(s)
        while before <= len(s)/2:
            l[before] = min(l[before], l[after])
            l[after] = l[before]
            before+=1
            after-=1
        return ''.join(l)
