class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        res,tot = 0,0
        for i in nums:
            res|=i
            tot+=i
            res|=tot
        return res
