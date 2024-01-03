from heapq import heappush, heappop
class Solution:
        def get_distance(self, worker, bike):
                return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

            bike_used = [0] * len(bikes)
            heap = [(0, 0, tuple(bike_used))]
            distance = {0: 0}
            while heap:
                curr_cost, curr_worker, bike_used = heappop(heap)
                if curr_worker == len(workers):
                    return curr_cost
                for i, bike in enumerate(bikes):
                    if bike_used[i]: continue
                    n_bike_used = bike_used[:i] + (1,) + bike_used[i+1:]
                    bike_state = tuple(n_bike_used)
                    next_cost = curr_cost + self.get_distance(workers[curr_worker], bikes[i])
                    if bike_state in distance and distance[bike_state] <= next_cost:
                        continue
                    heappush(heap, (next_cost, curr_worker + 1, bike_state))
                    distance[bike_state] = next_cost

            return -1
