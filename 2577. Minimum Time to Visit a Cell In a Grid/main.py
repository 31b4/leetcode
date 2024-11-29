import heapq
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        
        # If the starting point is blocked, return -1
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        heap = [(0, 0, 0)]  # (time, row, col)
        visited = [[False] * n for _ in range(m)]  # To track visited cells
        
        while heap:
            time, row, col = heapq.heappop(heap)
            
            # If we reach the bottom-right corner, return the time
            if row == m - 1 and col == n - 1:
                return time
            
            # Skip if already visited
            if visited[row][col]:
                continue
            visited[row][col] = True
            
            # Explore all directions
            for dr, dc in directions:
                r, c = row + dr, col + dc
                
                # Check bounds and if already visited
                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    if grid[r][c] <= time + 1:
                        heapq.heappush(heap, (time + 1, r, c))
                    else:
                        diff = grid[r][c] - time
                        if diff % 2 == 1:
                            heapq.heappush(heap, (grid[r][c], r, c))
                        else:
                            heapq.heappush(heap, (grid[r][c] + 1, r, c))
        
        # If no valid path is found, return -1
        return -1
