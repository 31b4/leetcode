class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj_list=[[] for _ in range(n)]
        for u,v,w in edges:
            self.adj_list[u].append((v,w))
        

    def addEdge(self, edge: List[int]) -> None:
        u,v,w=edge
        self.adj_list[u].append((v,w))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        n=len(self.adj_list)
        pq=[(0,node1)]
        dist=[float('inf') for _ in range(n)]
        dist[node1]=0
        while pq:
            d,u=heapq.heappop(pq)
            if u==node2:
                return d
            if d>dist[u]:
                continue
                
            for v,w in self.adj_list[u]:
                if d+w<dist[v]:
                    dist[v]=d+w
                    heapq.heappush(pq,(dist[v],v))

        return -1         
