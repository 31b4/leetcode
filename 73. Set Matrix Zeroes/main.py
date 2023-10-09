class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRows = set()
        zeroCols = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)
        
        for i in range(n):
            for j in range(m):
                if i in zeroRows or j in zeroCols:
                    matrix[i][j] = 0
