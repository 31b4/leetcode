class Solution:
    def minOperations(self, s: str) -> int:
        r0 = 0
        r1 = 0
        for i in range(len(s)):
            print(r0,r1,i)
            if i % 2:
                if s[i] == '1':
                    r0 += 1
            else:
                if s[i] == '0':
                    r0 += 1
            if i % 2:
                if s[i] == '0':
                    r1 += 1
            else:
                if s[i] == '1':
                    r1 += 1
        return min(r0,r1)
