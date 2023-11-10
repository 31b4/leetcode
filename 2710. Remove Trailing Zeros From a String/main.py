class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        #return num.strip("0")
        for i,x in enumerate(num[::-1]):
            if not x == "0":
                return num[:len(num)-i]
        return ''
