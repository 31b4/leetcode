class Trie:
    def __init__(self):
        self.score = 0
        self.children = {}

    def add(self, s: str, i: int):
        if (i): self.score += 1
        if (i == len(s)): return
        if (not self.children.get(s[i])): self.children[s[i]] = Trie()
        self.children[s[i]].add(s, i+1)

    def dfs(self, s: str, i: int):
        if (i == len(s)): return self.score
        return self.score + self.children[s[i]].dfs(s, i+1)
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word, 0)
        res = []
        for word in words:
            res.append(trie.dfs(word, 0))
        return res
        
