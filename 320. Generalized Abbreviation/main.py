class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        n = len(word)
        def dfs(i: int, cur: str) -> None:
            if i >= n:
                res.append(cur)
                return
            dfs(i + 1, cur + word[i])
            if cur and cur[-1].isnumeric(): return
            for j in range(i, n):
                dfs(j + 1, cur + str(j - i + 1))
        dfs(0, "")
        return res
