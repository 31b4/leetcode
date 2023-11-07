class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [dist[i] / speed[i] for i in range(len(dist))]
        time.sort()
        
        for i in range(len(time)):
            if time[i] <= i:
                return i

        return len(time)
