class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bin(n)[2] == "1" and bin(n).count("1") == 1
