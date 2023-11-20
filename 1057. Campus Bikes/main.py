class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)

        def manhattan(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        all_sorted = []
        for w_idx, worker in enumerate(workers):
            for b_idx, bike in enumerate(bikes):
                dist = manhattan(worker, bike)
                all_sorted.append((dist, w_idx, b_idx))

        all_sorted.sort()

        bike_status = [False] * m
        worker_status = [-1] * n
        pair_count = 0

        for distance, worker, bike in all_sorted:
            if worker_status[worker] == -1 and not bike_status[bike]:
                bike_status[bike] = True
                worker_status[worker] = bike
                pair_count += 1
                
                if pair_count == n:
                    return worker_status
        
        return worker_status
