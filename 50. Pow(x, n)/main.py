class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = self.myPow(x * x, abs(n) // 2) * (x if n % 2 else 1) if n else 1
        return p if n >= 0 else 1 / p
