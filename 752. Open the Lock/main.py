from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        pow10 = [1, 10, 100, 1000]
        visit = [0] * 10000  # 0: not visited, 1: visited through forward direction, -1: visited through backward direction, 2: deadends
        for dead in deadends:
            visit[int(dead)] = 2
        src, dest = 0, int(target)
        steps, dir = 0, 1
        if visit[src] == 2 or visit[dest] == 2:
            return -1
        if src == dest:
            return 0
        forward, backward = deque(), deque()
        forward.append(src)
        visit[src] = 1
        backward.append(dest)
        visit[dest] = -1
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                dir = -dir
            steps += 1
            size = len(forward)
            for _ in range(size):
                cur = forward.popleft()
                for p in pow10:
                    d = (cur // p) % 10
                    for i in [-1, 1]:
                        z = d + i
                        z = 9 if z == -1 else (0 if z == 10 else z)
                        next_combination = cur + (z - d) * p
                        if visit[next_combination] == -dir:
                            return steps
                        if visit[next_combination] == 0:
                            forward.append(next_combination)
                            visit[next_combination] = dir
        return -1
