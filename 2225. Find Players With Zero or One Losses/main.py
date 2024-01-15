class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss={}
        for p in matches:
            x, y=p
            if x not in loss: loss[x]=0
            if y in loss: loss[y]+=1
            else: loss[y]=1
        ans=[[], []]
        for i, f in loss.items():
            if f==0:
                ans[0].append(i)
            elif f==1:
                ans[1].append(i)
        
        return [sorted(ans[0]), sorted(ans[1])]
        
