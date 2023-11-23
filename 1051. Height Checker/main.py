class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        for i, x in enumerate(sorted(heights)):
            if not x == heights[i]:
                res +=1
        return res
