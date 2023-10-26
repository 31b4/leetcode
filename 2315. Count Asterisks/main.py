class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(x.count('*') for x in s.split('|')[::2])
