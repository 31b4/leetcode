class Solution:
    def maxFrequencyElements(self, a: List[int]) -> int:
        return (m:=max(f:=Counter(a).values()))*[*f].count(m)
