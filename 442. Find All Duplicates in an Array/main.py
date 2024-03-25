class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        res = set()
        for x in nums:
            if x in s:
                res.add(x)
            else:
                s.add(x)
        return res
