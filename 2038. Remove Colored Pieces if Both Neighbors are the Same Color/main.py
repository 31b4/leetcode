class Solution:
    def winnerOfGame(self, C: str) -> bool:
        a = 0
        b = 0
        for i in range(1,len(C)-1):
            s = C[i-1] + C[i] + C[i+1]
            if s == "AAA":
                a += 1
            elif s == "BBB":
                b += 1
        return a>b
