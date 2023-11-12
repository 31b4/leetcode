class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        reachable = []
        visited = {source}
        buses = set([frozenset(x) for x in routes])
        res = 0
        while True:
            if target in visited: 
                return res
            res += 1

            for bus in buses:
                if visited & bus:
                    reachable.append(bus)
            if not reachable:
                return -1
            while reachable:
                bus = reachable.pop()
                buses.discard(bus)
                visited |= bus
