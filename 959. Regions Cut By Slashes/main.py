class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []
        self.count = 0

    def regionsBySlashes(self, grid):
        n = len(grid)
        dots = n + 1
        self.parent = [i for i in range(dots * dots)]
        self.rank = [1] * (dots * dots)

        # Connect boundaries to the top-left corner (0,0)
        for i in range(dots):
            for j in range(dots):
                if i == 0 or j == 0 or i == n or j == n:
                    cell = i * dots + j
                    self.union(0, cell)

        # Process each cell and connect regions based on slashes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '\\':
                    cell1 = i * dots + j
                    cell2 = (i + 1) * dots + (j + 1)
                    self.union(cell1, cell2)
                elif grid[i][j] == '/':
                    cell1 = (i + 1) * dots + j
                    cell2 = i * dots + (j + 1)
                    self.union(cell1, cell2)

        return self.count

    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)
        if parentA == parentB:
            self.count += 1
        else:
            if self.rank[parentA] > self.rank[parentB]:
                self.parent[parentB] = parentA
            elif self.rank[parentA] < self.rank[parentB]:
                self.parent[parentA] = parentB
            else:
                self.parent[parentB] = parentA
                self.rank[parentA] += 1

    def find(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
