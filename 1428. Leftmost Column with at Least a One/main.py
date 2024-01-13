# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        x,y = binaryMatrix.dimensions()
        res = float('inf')
        for i in range(x):
            lo = 0
            hi = y-1
            idx = -1
            while lo <= hi:
                mid = (hi+lo) // 2
                val = binaryMatrix.get(i,mid)
                if val == 1:
                    idx = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            if idx != -1:
                res = min(res, idx)

        if res == float('inf'):
            return -1
        return res
