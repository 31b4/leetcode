class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [0]
        res = 0
        
        for s in arr:
            a, dup = 0, 0
            for c in s:
                dup |= a & (1 << (ord(c) - ord('a')))
                a |= 1 << (ord(c) - ord('a'))
            
            if dup > 0:
                continue
            
            for i in range(len(dp) - 1, -1, -1):
                if (dp[i] & a) > 0:
                    continue
                dp.append(dp[i] | a)
                res = max(res, bin(dp[i] | a).count('1'))
        
        return res
