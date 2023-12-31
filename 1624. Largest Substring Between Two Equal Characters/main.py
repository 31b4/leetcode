class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return max(s.rfind(ch) - s.find(ch) - 1 for ch in set(s))
