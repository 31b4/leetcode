class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        first = arr.get(0)
        n = arr.length()

        def findPeak(left, right):
            if left == right: return left
            mid = (left + right) // 2

            if arr.get(mid) > arr.get(max(mid - 1, 0)):
                return findPeak(mid + 1, right)
            else:
                return findPeak(left, mid)
        
        peak = findPeak(0, n - 1)
        left = 0
        right = peak - 1

        while left <= right:
            mid = (left + right) // 2
            x = arr.get(mid)

            if x == target:
                return mid
            elif x < target:
                left = mid + 1
            else:
                right = mid - 1
        
        left = peak
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            x = arr.get(mid)

            if x == target:
                return mid
            elif x < target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
