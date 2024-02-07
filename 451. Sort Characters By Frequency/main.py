class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        print(Counter(s))
        sort = [key for key, _ in freq.most_common()]

        res = ""
        for c in sort:
            res += freq[c]*c
        return res
