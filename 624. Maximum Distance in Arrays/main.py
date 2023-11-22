class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_val, min_val, res = float("-inf"), float("inf"), 0

        for arr in arrays:
            res = max(res, arr[-1] - min_val, max_val - arr[0])
            min_val = min(min_val,arr[0])
            max_val = max(max_val,arr[-1])
        return res
