class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #words.sort(key=len)
        d = defaultdict(int)

        for word in sorted(words,key = len):
            d[word] = 1
            for i in range(len(word)):
                w = word[:i] + word[i+1:]

                if w in d:
                    d[word] = max(d[word], d[w] +1)
        
        return max(d.values())