class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        res = 1
        for x in sorted(arr)[1:]:
            if x > res:
                res += 1
        return res
