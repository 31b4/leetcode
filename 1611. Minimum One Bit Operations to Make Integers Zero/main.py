class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        n = list(bin(n)[2:])
        cnt = 0
        for i in range(len(n) - 1, -1, -1):
            if n[i] == "0": continue
            else:
                cnt = - cnt - (2 ** (len(n) - i) - 1)
        return abs(cnt)
