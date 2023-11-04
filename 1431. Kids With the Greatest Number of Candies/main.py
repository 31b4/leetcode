class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [x+extraCandies >= max(candies)for x in candies]
