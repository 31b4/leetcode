class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        n = 1
        while k > (1 << n):
            k -= 1 << n
            n += 1
        return bin(k - 1)[2:].zfill(n).replace('0', '4').replace('1', '7')
