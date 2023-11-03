class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        best=0
        for i in range(1,n+1):
            if i in target:
                ans.append("Push")
                best=max(len(ans),best)
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans[:best]            
