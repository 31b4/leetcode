class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j=0
        for i in range(len(str1)):
            #print(i,j,str1[i],str2[j],(ord(str1[i])-97+1)%26,ord(str2[j])-97)
            if (ord(str1[i])-97+1)%26==ord(str2[j])-97 or str1[i]==str2[j]:
                j+=1
                if j==len(str2):
                    return True
        #print(j)
        return False
        
