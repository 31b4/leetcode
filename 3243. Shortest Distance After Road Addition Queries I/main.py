from heapq import heappop, heappush
from typing import List, Dict, Tuple

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Function to run Dijkstra's algorithm
        def dijkstra(start: int, end: int, graph: Dict[int, List[Tuple[int, int]]]) -> int:
            # Min-heap for priority queue
            heap = [(0, start)]  # (distance, node)
            distances = [float('inf')] * n
            distances[start] = 0
            
            while heap:
                curr_dist, curr_node = heappop(heap)
                
                # If we reach the destination, return the distance
                if curr_node == end:
                    return curr_dist
                
                # Skip if we find a longer distance in heap
                if curr_dist > distances[curr_node]:
                    continue
                
                # Explore neighbors
                for neighbor, weight in graph[curr_node]:
                    new_dist = curr_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heappush(heap, (new_dist, neighbor))
            
            # If unreachable, return infinity
            return distances[end]
        
        # Initialize graph as adjacency list
        graph = {i: [] for i in range(n)}
        for i in range(n - 1):
            graph[i].append((i + 1, 1))  # Unidirectional edge with weight 1
        
        result = []
        
        for u, v in queries:
            # Add the new road
            graph[u].append((v, 1))
            
            # Calculate shortest path from 0 to n-1
            shortest_path_length = dijkstra(0, n - 1, graph)
            result.append(shortest_path_length)
        
        return result
