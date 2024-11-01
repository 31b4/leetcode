from collections import Counter
from collections import defaultdict
class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = defaultdict(Counter)
        for i,c in enumerate(s):
            for a in 'abcdefghijklmnopqrstuvwxyz':
                prefix[i][a] += prefix[i-1][a] if i else 0
            prefix[i][c] += 1
        res = []
        for i,j in queries:
            cnt = 0
            for c in 'abcdefghijklmnopqrstuvwxyz':
                k = prefix[j][c] - (prefix[i-1][c] if i else 0)
                cnt += k*(k+1)//2
            res.append(cnt)
        return res


        
