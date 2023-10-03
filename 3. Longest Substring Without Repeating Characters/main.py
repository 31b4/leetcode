class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        ans = 0
        for i,x in enumerate(s):
            sv = x
            for y in s[i+1:]:
                if not y in sv:
                    sv += y
                else:
                    break
            ans = max(ans,len(sv))
        return ans
