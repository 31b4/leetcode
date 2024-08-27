class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Build the graph
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        # Max heap to store the max probability to reach each node
        max_heap = [(-1.0, start_node)]
        # Probability to reach each node, initialized with 0
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        
        # Dijkstra-like algorithm using max heap
        while max_heap:
            current_prob, node = heapq.heappop(max_heap)
            current_prob = -current_prob
            
            # If we reach the end node, return the probability
            if node == end_node:
                return current_prob
            
            # Explore neighbors
            for neighbor, edge_prob in graph[node]:
                # Calculate the probability to reach the neighbor via this node
                new_prob = current_prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        # If we exhaust the heap and don't reach the end_node
        return 0.0
