class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        res = 0
        pattern = []
        notAdjacent = {
            1: {3: 2, 7: 4, 9: 5}, 3: {1: 2, 7: 5, 9: 6},
            7: {1: 4, 3: 5, 9: 8}, 9: {1: 5, 3: 6, 7: 8},
            2: {8: 5}, 8: {2: 5}, 4: {6: 5}, 6: {4: 5}, 5: {}
        }
        def numberOfPatternsHelper():
            nonlocal res
            patternLen = len(pattern)

            res += (m <= patternLen <= n)
            if patternLen == n: return

            for cur in range(1, 10):
                if cur in pattern:
                    continue
                if pattern:
                    last = pattern[-1]
                    keysNotAllowed = notAdjacent[last]
                    if cur in keysNotAllowed and not keysNotAllowed[cur] in pattern:
                        continue

                pattern.append(cur)
                numberOfPatternsHelper()
                pattern.pop()

        numberOfPatternsHelper()
        return res
        
