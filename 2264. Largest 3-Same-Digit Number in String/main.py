class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1,-1):
            if str(i)*3 in num:
                return str(i)*3
        return ""
