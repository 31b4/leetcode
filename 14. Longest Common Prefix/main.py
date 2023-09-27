class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref= ""
        sv =""
        for i,x in enumerate(strs[0]):
            sv += x
            for j in range(1, len(strs)):
                if strs[j][:i+1] != sv:
                   return pref 
            pref = sv
        return pref
