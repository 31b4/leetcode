class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        l = [x[::-1] for x in l]
        l.sort()
        l = [x[::-1] for x in l]

        return " ".join([x[:-1] for x in l])
