class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def multiply_matrices(A, B):
            rows_A, cols_A = len(A), len(A[0])
            rows_B, cols_B = len(B), len(B[0])
            
            result = [[0] * cols_B for _ in range(rows_A)]
            
            for i in range(rows_A):
                for j in range(cols_B):
                    for k in range(cols_A):
                        result[i][j] += A[i][k] * B[k][j] % MOD
            
            return result

        def matrix_power(matrix, n):
            result = [
                [1 if i == j else 0
                 for j in range(len(matrix))] 
                    for i in range(len(matrix))
            ]

            base = matrix
            while n > 0:
                if n % 2 == 1:
                    result = multiply_matrices(result, base)
                base = multiply_matrices(base, base)
                n //= 2
            
            return result

        transitions = [
            [0, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0]
        ]

        paths_matrix = matrix_power(transitions, n - 1)
        initial_state = [1, 1, 1, 0, 0, 0, 0]

        final_state = [
            sum(initial_state[j] * paths_matrix[j][i] % MOD
                 for j in range(len(initial_state)))
                    for i in range(len(paths_matrix[0]))]
    
        total_paths = sum(final_state)
        return total_paths % MOD
