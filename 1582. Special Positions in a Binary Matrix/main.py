class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if sum(mat[i]) == 1 and sum(mat[k][j] for k in range(m)) == 1:
                        res += 1

        return res
