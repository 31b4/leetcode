class Solution:
    @cache
    def numRollsToTarget(self, n: int, k: int, t: int) -> int:
                return sum(self.numRollsToTarget(n-1, k, t-f) for f in range(1, k+1))%(10**9+7) if n else t == 0
