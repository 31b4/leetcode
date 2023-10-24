class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        sv = 0
        for x in s:
            if x =="(":
                sv += 1
            if x == ")":
                res = max(res,sv)
                sv -= 1
        return res
