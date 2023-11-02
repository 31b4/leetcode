class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(x if x%m else -x for x in range(1,n+1))
