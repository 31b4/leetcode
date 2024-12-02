class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split the sentence into words
        words = sentence.split()
        
        # Iterate through each word along with its index
        for index, word in enumerate(words, start=1):  # Start indexing from 1
            # Check if the searchWord is a prefix of the current word
            if word.startswith(searchWord):
                return index
        
        # If no word matches, return -1
        return -1
