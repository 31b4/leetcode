class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        sum_rolles=sum(rolls)
        total=(n+m)*mean
        miss=total-sum_rolles
        if miss>6*n or miss<n: return []
        q,r=divmod(miss, n)
        return [q+1]*r+[q]*(n-r)
        
