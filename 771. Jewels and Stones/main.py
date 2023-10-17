class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(x in jewels for x in stones)
