class Solution:
    def subarraysDivByK(self, a: List[int], k: int) -> int:
        return (c:=Counter([0])) and sum(c.update([p%k]) or c[p%k]-1 for p in accumulate(a))
