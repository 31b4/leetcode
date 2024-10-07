class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        # Traverse each character in the string
        for char in s:
            # Add the current character to the stack
            stack.append(char)
            
            # Check if the last two characters form "AB" or "CD"
            if len(stack) >= 2:
                if (stack[-2] == 'A' and stack[-1] == 'B') or (stack[-2] == 'C' and stack[-1] == 'D'):
                    # If they do, pop them from the stack
                    stack.pop()  # remove the last character
                    stack.pop()  # remove the second last character
        
        # The remaining stack gives the minimized string length
        return len(stack)
