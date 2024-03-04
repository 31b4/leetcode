class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        r=scr=0
        tokens.sort()
        i,j= 0,len(tokens)-1
        while i<=j:
            if power>=tokens[i]:
                scr+=1
                power-=tokens[i]
                i+=1
                r=max(r,scr)
            elif scr>0:
                scr-=1
                power+=tokens[j]
                j-=1
            else: 
                break
        return r
