class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        for i in range(1,m):
            for j in range(m):
                matrix[i][j]+=min(matrix[i-1][k] for k in (j-1,j,j+1) if 0<=k and k<m)
        return min(matrix[-1])
