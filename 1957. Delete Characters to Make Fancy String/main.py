class Solution:
    def makeFancyString(self, s: str) -> str:
        # Initialize an empty list to build the result string
        result = []
        
        for char in s:
            # Only add char if it does not form three consecutive same characters
            if len(result) < 2 or not (result[-1] == result[-2] == char):
                result.append(char)
        
        # Join the list into a string and return
        return ''.join(result)
