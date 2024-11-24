class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        parity_neg, min_abs_num, sum_abs_num  = 0, inf, 0
        for row in matrix:
            for num in row:
                parity_neg ^= (num < 0)
                min_abs_num = min(abs(num), min_abs_num)
                sum_abs_num += abs(num)
        return sum_abs_num - parity_neg * min_abs_num * 2
