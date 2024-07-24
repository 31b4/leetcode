class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        mapping = defaultdict(list)
        for a,b,c in highways:
            mapping[a].append((b,c))
            mapping[b].append((a,c))

        heap = [(0, -discounts, 0)]
        visited = [[float("inf")] * (discounts + 1) for _ in range(n)]
        while heap:
            cost, k, node = heappop(heap)
            if node == n - 1: return cost
            if visited[node][-k] < cost: continue
            for child, toll in mapping[node]:
                if cost + toll < visited[child][-k]:
                    visited[child][-k] = cost + toll
                    heappush(heap, (cost + toll, k, child))
                if k != 0 and cost + toll // 2 < visited[child][-(k+1)]:
                    visited[child][-(k+1)] = cost + toll // 2
                    heappush(heap, (cost + toll // 2, k + 1, child))
        return -1
