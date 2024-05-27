class Solution:
    def specialArray(self, a: List[int]) -> int:
        return a.sort() or next((x for l,x,r in zip([-inf]+a,count(len(a),-1),a) if l<x<=r),-1)
