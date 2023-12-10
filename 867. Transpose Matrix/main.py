class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            sv = []
            for j in range(len(matrix)):
                sv.append(matrix[j][i])
            res.append(sv)
        return res
