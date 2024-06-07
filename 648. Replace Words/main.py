class Solution:
    def replaceWords(self, d: List[str], s: str) -> str:
        s=s.split(' ')
        d.sort()
        ans=""
        for i in s:
            flg=False
            for j in d:
                if i.startswith(j):
                    ans+=j+' '
                    flg=True
                    break
            if not flg:
                ans+=i+' '
        return ans[:-1]
