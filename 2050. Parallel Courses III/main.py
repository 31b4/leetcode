class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        for u, v in relations:
            graph[u].append(v)
            in_degree[v] += 1 
        dist = [0] + time
        queue = deque([i for i in range(1, n+1) if in_degree[i] == 0])
        
        while queue:
            course = queue.popleft()
            for next_course in graph[course]:
                dist[next_course] = max(dist[next_course], dist[course] + time[next_course-1])
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return max(dist)
