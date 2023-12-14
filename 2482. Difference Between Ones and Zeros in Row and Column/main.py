class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        row, col = [0] * R, [0] * C
        for r in range(R):
            for c in range(C):
                offset = 2 * grid[r][c] - 1
                row[r] += offset
                col[c] += offset
        return [[row[r] + col[c] for c in range(C)] for r in range(R)]
