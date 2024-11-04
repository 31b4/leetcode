class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        n = len(word)
        
        while i < n:
            # Get the current character
            char = word[i]
            # Count the number of consecutive chars up to 9
            count = 0
            while i < n and word[i] == char and count < 9:
                count += 1
                i += 1
            # Append the count and character to the result string
            comp += str(count) + char
        
        return comp
