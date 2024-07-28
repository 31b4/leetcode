class Solution:

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        g = [[] for _ in range(n + 1)]

        for u, v in edges:

            g[u].append(v)

            g[v].append(u)

        

        q = deque([(1, 1)])

        dist1 = [-1] * (n + 1)

        dist2 = [-1] * (n + 1)

        dist1[1] = 0

        while q:

            x, freq = q.popleft()

            t = dist1[x] if freq == 1 else dist2[x]

            if (t // change) % 2:

                t = change * (t // change + 1) + time

            else:

                t += time

            for y in g[x]:

                if dist1[y] == -1:

                    dist1[y] = t

                    q.append((y, 1))

                elif dist2[y] == -1 and dist1[y] != t:

                    if y == n:

                        return t

                    dist2[y] = t

                    q.append((y, 2))

        return 0

        
