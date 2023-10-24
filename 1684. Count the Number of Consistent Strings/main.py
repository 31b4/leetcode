class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(1 for x in words if set(x).issubset(set(allowed)))
