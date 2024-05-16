class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        self.count = 0

        def is_valid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False

        def get_next_cell(i, j, direction):
            pos = [(i,j+1), (i+1,j), (i,j-1), (i-1,j)]
            return pos[direction]

        def dfs(i, j, visited, direction, cleaned):
            if (i,j) not in cleaned:
                self.count+=1
                cleaned.add((i,j))
            visited.add((i,j, direction))
            x, y = get_next_cell(i,j,direction)
            # try to move forward
            if is_valid(x, y) and room[x][y] == 0:
                if (x,y, direction) in visited:
                    return
                dfs(x, y, visited, direction, cleaned)
            else:
                # obstacle or end of room is reached
                # turn right and try to move forward
                for k in range(1, 4):
                    x, y = get_next_cell(i, j, (direction+k)%4)
                    if is_valid(x, y) and room[x][y] == 0:
                        if (x, y, (direction+k)%4) in visited:
                            return
                        dfs(x, y, visited, (direction+k)%4, cleaned)
                        break
        dfs(0, 0, set(), 0, set())
        return self.count
                
