class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0  # Start both pointers at the beginning of s and t
        
        while i < len(s) and j < len(t):  # Continue until one of the strings is fully scanned
            if s[i] == t[j]:  # If characters match
                j += 1  # Move the pointer in t forward
            i += 1  # Always move the pointer in s forward
        
        return len(t) - j  # The number of characters in t not matched in s
               
