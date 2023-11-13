class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        l, r = 0, len(s)
        for char in s:
            if char == 'I':
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        return res + [l]
        
