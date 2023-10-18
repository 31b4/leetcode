class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(1 for i in text.split(' ') if not any(j in i for j in brokenLetters))
