class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, w in roads: # TC: O(E), SC: O(E)
            graph[u - 1].append((v - 1, w))
            graph[v - 1].append((u - 1, w))
        
        ans = [float('inf') for _ in range(n)]
        for i in range(n): # TC: O(V)
            dist = [float('inf') for _ in range(n)]
            dist[i] = 0
            pq = [(0, i)]
            while pq:
                d, u = heapq.heappop(pq) # TC: (logV)
                ans[i] = min(ans[i], appleCost[u] + (k + 1) * d)
                for v, w in graph[u]: # TC: O(V)
                    temp_d = d + w
                    if temp_d < dist[v]: 
                        dist[v] = temp_d
                        heapq.heappush(pq, (temp_d, v)) # TC:log(V)
        return ans
