class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        d = {}
        for c in candies[k:]:
            d[c] = d.get(c, 0) + 1
        
        res = len(d)
        for j in range(k, len(candies)):
            d[candies[j]] -= 1
            d[candies[j - k]] = d.get(candies[j - k], 0) + 1
            if d[candies[j]] == 0: d.pop(candies[j])
            res = max(res, len(d))
        return res
