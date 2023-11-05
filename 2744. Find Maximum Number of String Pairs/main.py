class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        new_words = [''.join(sorted(word)) for word in words]
        return len(new_words) - len(set(new_words))  
