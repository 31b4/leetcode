class Solution:
    def numberOfWays(self, corridor: str) -> int:
        S = 0
        P = 0
        res = 1
        
        for letter in corridor:
            if letter == "S":
                S += 1
                if S % 2 == 0 or S == 1:
                    P = 0
                else:
                    res = res * (P + 1)
                    res = res % (10 ** 9 + 7)
            else:
                P += 1

        return res if S != 0 and S % 2 == 0 else 0
