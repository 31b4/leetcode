class Solution:
    def pathSum(self, nums: List[int]) -> int:
        indexes = [
            int(str(x)[:2]) for x in nums
        ]
        values = dict(
            (
                int(str(x)[:2]),
                int(str(x)[2])
            ) for x in nums
        )
        for idx in indexes:
            next_left = (idx // 10) * 10 + 10 + (2 * (idx % 10) - 1) 
            next_right = (idx // 10) * 10 + 10 + (2 * (idx % 10))
            if next_left in values:
                values[next_left] += values[idx]
            if next_right in values:
                values[next_right] += values[idx]
        result = 0
        for idx in indexes:
            next_left = (idx // 10) * 10 + 10 + (2 * (idx % 10) - 1) 
            next_right = (idx // 10) * 10 + 10 + (2 * (idx % 10))
            if next_left not in values and next_right not in values:
                result += values[idx]
        return result
