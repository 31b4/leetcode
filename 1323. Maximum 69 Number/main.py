class Solution:
    def maximum69Number (self, num: int) -> int:
        sv = list(str(num))
        for i,x in enumerate(sv):
            if x == "6":
                sv[i] = "9"
                break
        return int("".join(sv))
