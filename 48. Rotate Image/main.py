class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i+1):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        for l in matrix:
            l.reverse()
