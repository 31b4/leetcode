class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n: return -1

        def f(d):
            len, bouquet=0, 0
            i=0
            while i<n:
                while i<n and bloomDay[i]<=d:
                    len+=1
                    if len==k:
                        bouquet+=1
                        len=0
                    i+=1
                if i<n and bloomDay[i]>d: len=0
                if bouquet>m: return True
                i+=1
            return bouquet>=m

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if f(mid):
                r = mid
            else:
                l = mid + 1
        return l

