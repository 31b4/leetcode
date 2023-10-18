class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(x.split(" ")) for x in sentences)
        return max(x.count(" ") for x in sentences)+1
