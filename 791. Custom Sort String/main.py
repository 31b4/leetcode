class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        ctr = Counter(s)

        ans = [ch*ctr[ch] for ch in order]

        ans.extend(filter(lambda x: x not in order,s))
        
        return ''.join(ans)
        
