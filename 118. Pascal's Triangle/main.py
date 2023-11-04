class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            row = [1] * (i + 1)
            for j in range(1, len(row) - 1):
                row[j] = ans[i - 1][j - 1] + ans[i - 1][j]
            ans.append(row)
        return ans
