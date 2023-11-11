class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0

        for i in range(min(n, limit) + 1):
            max_j = min(n - i, limit)
            min_k = max(0, n - i - limit)
            max_k = min(n - i, limit)

            count += max(0, max_k - min_k + 1)

        return count
