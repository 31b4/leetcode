from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        positions = defaultdict(list)
        for i, c in enumerate(ring):
            positions[c].append(i)
        return self.helper(0, 0, positions, key, ring, memo)
    
    def helper(self, in_index, pos, positions, key, ring, memo):
        if in_index == len(key):
            return 0
        if (in_index, pos) in memo:
            return memo[(in_index, pos)]
        min_steps = float('inf')
        for i in positions[key[in_index]]:
            if i >= pos:
                steps = min(i - pos, pos + len(ring) - i)
            else:
                steps = min(pos - i, i + len(ring) - pos)
            min_steps = min(min_steps, steps + self.helper(in_index + 1, i, positions, key, ring, memo))
        memo[(in_index, pos)] = min_steps + 1
        return min_steps + 1
