class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # lets loop in s
        res = []
        p_sorted = sorted(p)
        for i in range(len(s)-len(p)+1):
            #we gonna check s[i:i+len(p)] in sorted is equal to sorted(p)
            #so we have "bcaqqq" ans "abc"
            # we gonna check if sorted("bca") = "abc" == sorted("abc")        
            if sorted(s[i:i + len(p)]) == p_sorted:
                res.append(i)
        return res
