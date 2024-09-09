class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        N, M = len(slots1), len(slots2)
        i, j = 0, 0

        while (i < N and j < M):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]

            if (s1 <= e2 or s2 <= e1):
                max_start = max(s1, s2)
                min_end = min (e1, e2)
                if (min_end - max_start >= duration):
                    return ([max_start, max_start+duration])
            
            if (e1 < e2):
                i += 1
            else:
                j += 1

        return []
