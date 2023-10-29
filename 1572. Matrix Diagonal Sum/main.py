class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n):
            ans += mat[i][i]
            if not i == n-i-1:
                ans += mat[i][n-i-1]
        return ans
