class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        prev = 0
        res = 0
        for c in word:
            i = keyboard.index(c)
            res += abs(prev - i)
            prev = i
        return res
