class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        sub = ""
        if len(s) % 2 == 1:
            sub = s[-1]
        return "".join(s[i] + chr(ord(s[i])+int(s[i+1])) for i in range(0,len(s)-1,2))+sub
