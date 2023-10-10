class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def is_valid_move():
            # Check if the next move is within bounds and not visited
            next_i = i + directions[curr_dir][0]
            next_j = j + directions[curr_dir][1]
            return (
                0 <= next_i < len(matrix)
                and 0 <= next_j < len(matrix[0])
                and (next_i, next_j) not in visited
            )

        ans = []
        visited = set()  # Store visited positions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        curr_dir = 0  # Index of the current direction
        i, j = 0, 0  # Starting position

        if len(matrix[0]) == 1:
            # Handle a special case when there is only one column
            return [num for row in matrix for num in row]

        while len(ans) < len(matrix) * len(matrix[0]):
            ans.append(matrix[i][j])
            visited.add((i, j))

            i += directions[curr_dir][0]
            j += directions[curr_dir][1]
            
            if not is_valid_move():
                # If it's time to turn, increment the current direction index
                curr_dir = (curr_dir + 1) % 4
                
        return ans
