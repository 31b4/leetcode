from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cChars = Counter(chars)
        return sum(len(w) for w in words if not (Counter(w) - cChars))
