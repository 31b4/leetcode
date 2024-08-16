class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:

        abdiff = lambda y: abs(y[0] - y[1])

        f = lambda x: sum(map(abdiff, enumerate(sorted(x))))

        row, col = zip(*rooks)

        return f(row) + f(col)
