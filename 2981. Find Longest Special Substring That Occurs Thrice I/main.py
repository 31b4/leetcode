class Solution:
    def maximumLength(self, s: str) -> int:
        # Helper function to check if a string is special
        def is_special(sub: str) -> bool:
            return len(set(sub)) == 1  # A string is special if all characters are the same
        
        n = len(s)
        max_length = -1  # Initialize the result as -1
        
        # Iterate over all substrings
        for length in range(1, n + 1):  # Substring lengths from 1 to n
            substr_count = {}
            
            for i in range(n - length + 1):  # Starting points for substrings of current length
                substring = s[i:i + length]
                
                if is_special(substring):  # Check if substring is special
                    # Count occurrences of the substring
                    substr_count[substring] = substr_count.get(substring, 0) + 1
                    
                    # Update max_length if the substring occurs at least three times
                    if substr_count[substring] >= 3:
                        max_length = max(max_length, length)
        
        return max_length
