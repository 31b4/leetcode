class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 0
        for x in s[::-1]:
            if x == ' ' and n > 0:
                return n
            elif x != ' ':
                n+=1
        return n
