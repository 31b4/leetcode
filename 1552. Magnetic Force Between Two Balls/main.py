class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def canPlaceBalls(d):
            count = 1  # Place the first ball
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= d:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False

        left, right = 1, position[-1] - position[0]
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
