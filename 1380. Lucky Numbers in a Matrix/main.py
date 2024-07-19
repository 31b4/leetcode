class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        rows: int = len(matrix)
        cols: int = len(matrix[0])

        row_minimums: list[int] = [10**5 + 1 for _ in range(rows)]
        col_maximums: list[int] = [0 for _ in range(cols)]

        for row_ind in range(rows):
            for col_ind in range(cols):
                el: int = matrix[row_ind][col_ind]
                row_minimums[row_ind] = min(row_minimums[row_ind], el)
                col_maximums[col_ind] = max(col_maximums[col_ind], el)

        for row_ind in range(rows):
            for col_ind in range(cols):
                el: int = matrix[row_ind][col_ind]
                if el == row_minimums[row_ind] == col_maximums[col_ind]:
                    return [el]
        return []
