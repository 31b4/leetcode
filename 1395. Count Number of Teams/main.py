class Solution:

    # alt, for perf test

    def numTeams(self, rating: List[int]) -> int:

        l = []

        sr = sorted(rating)

        low = {}

        for idx,r in enumerate(sr):

            low[r] = idx

        res = 0

        n = len(rating)

        for idx,r in enumerate(rating):

            i = bisect.bisect(l, r)

            l.insert(i,r)

            j = low[r] - i

            res+=i*(n-1-idx-j)+j*(idx-i)

        return res

    def numTeams2(self, rating: List[int]) -> int:

        ans,n = 0,len(rating)

        for j in range(n):

            # for any middle position j find counts less than rating[j] in  [0..j) and (j..n) ranges

            llt,lgt = 0,0

            for i in range(j):

                llt += rating[i] < rating[j]

                lgt += rating[i] > rating[j]

            rlt,rgt = 0,0

            for k in range(j+1,n):

                rlt += rating[k] < rating[j]

                rgt += rating[k] > rating[j]

            ans += llt*rgt + lgt*rlt 

        return ans

    # bf,tle

    def numTeams1(self, rating: List[int]) -> int:

        ans,n = 0,len(rating)

        for i in range(n):

            for j in range(i+1,n):

                for k in range(j+1,n):

                    ans += 1 if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k] else 0

        return ans      
