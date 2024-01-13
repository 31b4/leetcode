class Solution:
    def minSteps(self, s: str, t: str) -> int:
        for x in s:
            try:
                i = t.index(x)
                t = t[:i] + t[i+1:]
                del t[i]
            except:
                pass
        print(t)
        return len(t)
