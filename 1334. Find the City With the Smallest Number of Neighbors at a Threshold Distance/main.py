class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # first convert graph to adjacency list representation
        graph: list[list[int]] = [[] for _ in range(n)]  # i-th nodes will have graph[i] neighbors
        for node1, node2, distance in edges:
            graph[node1].append([node2, distance])
            graph[node2].append([node1, distance])

        def get_number_of_neighbors_in_distance(source: int) -> int:
            queue: list[tuple[int, int]] = [
                (0, source)
            ]  # distance to node itself is 0, first store distance so heap is "sorted" b distance
            visited = set()

            while queue:
                distance_to_this_node, cur_node = heappop(queue)
                if not cur_node in visited:
                    visited.add(cur_node)
                    for neighbor, distance in graph[cur_node]:
                        distance_from_source = distance_to_this_node + distance
                        if distance_from_source <= distanceThreshold:  # ensure that we're allowed to go to this node
                            heappush(queue, (distance_from_source, neighbor))

            # actually you can return len(visited) and with math there will be nothing wrong but actually we have len(visited) - 1 neighbors since we're not neighbor of ourselves
            return len(visited) - 1

        minimum_number: int = n
        res: int = None

        for source in range(n):
            neighbors: int = get_number_of_neighbors_in_distance(source)
            # we iterate source from smaller to bigger this ensures that we choose node with greater value if they have equal number of neighbors
            if neighbors <= minimum_number:
                minimum_number = neighbors
                res = source

        return res
