class Solution:
    def maxSumAfterPartitioning(self, a: List[int], k: int) -> int:
        @cache
        def calc(i, m, l):
            if i != len(a):
                m = max(m,a[i])
                l += 1
                # end of part
                r = m*l + calc(i+1, 0, 0)
                if l < k:
                    # continue part
                    r = max(r, calc(i+1, m, l))
            
                return r
                
            return m*l
        
        return calc(0, 0, 0)
