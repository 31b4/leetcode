class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        more_than = len(arr) * 0.25
        for x in set(arr):
            if arr.count(x) > more_than:
                return x 
