class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word[:word.index(ch)+1][::-1] + word[word.index(ch)+1:] if ch in word else word
