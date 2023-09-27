class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        r = ['I', 'IV','V', 'IX','X', 'XL','L', 'XC','C', 'CD','D','CM', 'M']
        n = [1,4, 5, 9,10,40, 50, 90,100, 400,500,900, 1000]
        i = 0
        while i < len(s):
            try:
                ans += n[r.index(s[i]+s[i+1])]
                i+=1
            except:
                ans += n[r.index(s[i])]
            i+=1
        return  ans
