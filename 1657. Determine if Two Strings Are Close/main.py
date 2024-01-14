class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1)==set(word2) and sorted(Counter(word1).values())==sorted(Counter(word2).values())
        
