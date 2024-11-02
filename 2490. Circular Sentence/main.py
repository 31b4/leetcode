class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split the sentence into words
        words = sentence.split()
        
        # Number of words in the sentence
        n = len(words)
        
        # Check the circular condition
        for i in range(n):
            # Last character of the current word
            last_char = words[i][-1]
            # First character of the next word (wrapping around using modulo)
            first_char_next = words[(i + 1) % n][0]
            
            # If they don't match, sentence is not circular
            if last_char != first_char_next:
                return False
        
        # If all pairs satisfy the condition, return True
        return True
