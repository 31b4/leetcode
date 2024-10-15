class Solution:
    def minimumSteps(self, s: str) -> int:
        white=0
        res=0
        j=0
        n=len(s)
        while(j<n):
            if s[j]=='0':
                res+=white
            white+=1 if s[j]=='1' else 0
            j+=1
            
            
        return res
