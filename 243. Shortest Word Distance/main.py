class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d = defaultdict(list)
        for i, val in enumerate(wordsDict):
            d[val].append(i)
        return min(abs(x - y) for x in d[word1] for y in d[word2])        
