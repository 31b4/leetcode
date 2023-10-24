class Solution:
    def toLowerCase(self, s: str) -> str:
        for i in range(len(s)):
            # If s[i] is uppercase, convert it to lowercase.
            if 65 <= ord(s[i]) <= 90:
                s = s[:i] + chr(ord(s[i]) + 32) + s[i+1:]
        return s
