class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        i = 0
        res = []
        while len(res) < len(nums):
            res.append(pos[i])
            if i < len(neg):
                res.append(neg[i])
            i += 1
        return res
