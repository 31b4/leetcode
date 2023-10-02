class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.index(x) for x in s] == [t.index(x) for x in t]
