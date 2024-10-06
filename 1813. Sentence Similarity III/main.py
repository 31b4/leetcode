class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split both sentences into words
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        # Ensure sentence1 is the shorter one, swap if necessary
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        
        # Try to match the words from the start
        i = 0
        while i < len(words1) and words1[i] == words2[i]:
            i += 1
        
        # Try to match the words from the end
        j = 0
        while j < len(words1) and words1[-(j+1)] == words2[-(j+1)]:
            j += 1
        
        # If the matched prefix and suffix together cover all of words1, return true
        return i + j >= len(words1)
