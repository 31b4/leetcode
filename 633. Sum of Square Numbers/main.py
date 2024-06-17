from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):  # Iterate through all possible values of `a`
            b = sqrt(c - a * a)  # Compute `b` as the square root of `c - a^2`
            if b == int(b):  # Check if `b` is an integer
                return True  # If `b` is an integer, return true
        return False  # If no such pair `(a, b)` is found, return false
